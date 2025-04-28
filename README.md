# sqlalchemy-altibase7
- Altibase support for SQLAlchemy implemented as an external dialect.
- It is tested on Altibase v7.
- This source code is maintained on https://github.com/hesslee/sqlalchemy-altibase7
- This source code is based on https://pypi.org/project/sqlalchemy-altibase
- This package is uploaded on https://pypi.org/project/sqlalchemy-altibase7

# Changes from sqlalchemy-altibase
- It is mainly supplemented for langchain connectivity.
- sqlalchemy version upper limit requirement is removed.

## Prereqisite
- Download and install Altibase server and client from http://support.altibase.com/en/product
- Unixodbc setting for Linux
- ODBC DSN setting for Windows

### Unixodbc setting example for Linux
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

### ODBC DSN setting example for Windows
- Altibase Windows ODBC driver is registered during Altibase Windows client installation procedure.
- Add a ODBC DSN for Altibase.
- example configuration :
```
[Altibase Connection Config]
Windows DSN Name: PYODBC
host(name or IP): 192.168.1.210
Port(default 20300): 21121
User: SYS
Password: MANAGER
Database: mydb
NLS_USE: UTF-8
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


