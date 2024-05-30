from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

# connectstring: altibase+pyodbc://<username>:<password>@<dsnname>?server=<server> & port=<port> & database=<database_name>
db = SQLDatabase.from_uri("altibase+pyodbc://@PYODBC?encoding=UTF-8")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

response = agent_executor.invoke({"input": "List the total sales per country. Which country's customers spent the most?"})
#response = agent_executor.invoke({"input": "Describe the playlisttrack table"})
print(response)

