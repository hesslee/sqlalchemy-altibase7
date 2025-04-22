# sqlalchemy-altibase7
- Altibase support for SQLAlchemy implemented as an external dialect.
- It is tested on Altibase v7.
- This source code is based on https://pypi.org/project/sqlalchemy-altibase .
- This package itself is uploaded on https://pypi.org/project/sqlalchemy-altibase7 .

# Changes from sqlalchemy-altibase
- It is mainly supplemented for langchain connectivity.
- sqlalchemy version upper limit requirement is removed.

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

# sqlalchemy-altibase7 using langchain
- install : pip install sqlalchemy-altibase7
- reference : https://python.langchain.com/v0.1/docs/use_cases/sql/
- test preparation : Populate sample data into Altibase database using "test/Chinook_Altibase.sql" file in this repository.
- test programs
  - langchain_chain.py : using chain
    - reference : https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/#chain
  - langchain_agent.py : using sql agent
    - reference : https://python.langchain.com/v0.1/docs/use_cases/sql/agents/#agent
  - langchain_agent_fewshot.py : using sql agent with few shot prompt
    - reference : https://python.langchain.com/v0.1/docs/use_cases/sql/agents/#using-a-dynamic-few-shot-prompt
  - langchain_agent_retriever.py : using sql agent with retriever for correcting invalid nouns
    - reference : https://python.langchain.com/v0.1/docs/use_cases/sql/agents/#dealing-with-high-cardinality-columns


