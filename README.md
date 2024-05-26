# sqlalchemy-altibase7
- Altibase support for SQLAlchemy implemented as an external dialect.
- It is test on Altibase v7.
- It is mainly supplemented for langchain connectivity.
- This source code is based on https://pypi.org/project/sqlalchemy-altibase .
- This package itself is uploaded on https://pypi.org/project/sqlalchemy-altibase7 .

# Prereqisite
- unixodbc
- pyodbc

## unixodbc
- install : sudo apt-get install unixodbc-dev
- example configuration :
```
$ cat /etc/odbc.ini 
[PYODBC]
Driver          = /home/hess/work/altidev4/altibase_home/lib/libaltibase_odbc-64bit-ul64.so
Database        = mydb
ServerType      = Altibase
Server          = 127.0.0.1
Port            = 21121
UserName        = SYS
Password        = MANAGER
FetchBuffersize = 64
ReadOnly        = no

$ cat /etc/odbcinst.ini 
[ODBC]
Trace=Yes
TraceFile=/tmp/odbc_trace.log
```

## pyodbc
- install : pip install pyodbc
- test :
```
$ python
>>> import pyodbc
>>> conn = pyodbc.connect('DSN=PYODBC')
>>> curs = conn.cursor()
>>> curs.execute("select * from v$table")
>>> curs.fetchall()
```

#### sqlalchemy-altibase7 using langchain
- install : pip install sqlalchemy-altibase7
- reference : https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/
- test preparation : Populate sample data into Altibase database using "test/Chinook_Altibase.sql" file in this repository.
- test :
```
$ python
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

# connectstring: altibase+pyodbc://<username>:<password>@<dsnname>?server=<server> & port=<port> & database=<database_name>
db = SQLDatabase.from_uri("altibase+pyodbc://@PYODBC")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many employees are there?"})
print(response)
```

