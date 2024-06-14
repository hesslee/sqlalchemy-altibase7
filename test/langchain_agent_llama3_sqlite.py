from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_experimental.llms.ollama_functions import OllamaFunctions

# connectstring: altibase+pyodbc://<username>:<password>@<dsnname>?server=<server> & port=<port> & database=<database_name>
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm = OllamaFunctions(model="llama3", format="json")

#agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
agent_executor = create_sql_agent(llm, db=db, agent_type="tool-calling", verbose=True)

response = agent_executor.invoke({"input": "List the total sales per country. Which country's customers spent the most?"})
#response = agent_executor.invoke({"input": "Describe the playlisttrack table"})
print(response)
