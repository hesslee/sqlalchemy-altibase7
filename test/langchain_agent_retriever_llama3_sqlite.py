from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# connectstring: altibase+pyodbc://<username>:<password>@<dsnname>?server=<server> & port=<port> & database=<database_name>
db = SQLDatabase.from_uri("altibase+pyodbc://@PYODBC?encoding=UTF-8")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

import ast
import re

def query_as_list(db, query):
    res = db.run(query)
    res = [el for sub in ast.literal_eval(res) for el in sub if el]
    res = [re.sub(r"\b\d+\b", "", string).strip() for string in res]
    return list(set(res))

artists = query_as_list(db, "SELECT Name FROM Artist")
albums = query_as_list(db, "SELECT Title FROM Album")

from langchain.agents.agent_toolkits import create_retriever_tool

vector_db = FAISS.from_texts(artists + albums, OpenAIEmbeddings())
retriever = vector_db.as_retriever(search_kwargs={"k": 5})
description = """Use to look up values to filter on. Input is an approximate spelling of the proper noun, output is \
valid proper nouns. Use the noun most similar to the search."""
retriever_tool = create_retriever_tool(
    retriever,
    name="search_proper_nouns",
    description=description,
)

system = """You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

If you need to filter on a proper noun, you must ALWAYS first look up the filter value using the "search_proper_nouns" tool! 

You have access to the following tables: {table_names}

If the question does not seem related to the database, just return "I don't know" as the answer."""

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

prompt = ChatPromptTemplate.from_messages(
    [("system", system), ("human", "{input}"), MessagesPlaceholder("agent_scratchpad")]
)
agent = create_sql_agent(
    llm=llm,
    db=db,
    extra_tools=[retriever_tool],
    prompt=prompt,
    agent_type="openai-tools",
    verbose=True,
)

response = agent.invoke({"input": "How many albums does alis in chain have?"})
print(response)

