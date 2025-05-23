from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from operator import itemgetter

# connectstring: altibase+pyodbc://<username>:<password>@<dsnname>?server=<server> & port=<port> & database=<database_name>
db = SQLDatabase.from_uri("altibase+pyodbc://@PYODBC?encoding=UTF-8")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

_altibase_prompt = """You are a Altibase expert. Given an input question, first create a syntactically correct Altibase query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per Altibase. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use TRUNC(SYSDATE) function to get the current date, if the question involves "today".
Never use ";", if it is not absolutely necessary.


Use the following format:


Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"


Only use the following tables:
{table_info}

Question: {input}"""


ALTIBASE_PROMPT = PromptTemplate(
   input_variables=["input", "table_info", "top_k"],
   template=_altibase_prompt,
)

execute_query = QuerySQLDataBaseTool(db=db)
write_query = create_sql_query_chain(llm, db, prompt = ALTIBASE_PROMPT)

#chain = write_query | execute_query
#response = chain.invoke({"question": "How many employees are there?"})
#print(response)

answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)

answer = answer_prompt | llm | StrOutputParser()
chain = (
    RunnablePassthrough.assign(query=write_query).assign(
        result=itemgetter("query") | execute_query
    )
    | answer
)

response = chain.invoke({"question": "How many employees are there"})
print(response)