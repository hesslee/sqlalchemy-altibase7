# sqlalchemy-altibase7
- Altibase support for SQLAlchemy implemented as an external dialect.
- It is test on Altibase v7.
- Mainly langchain connectivity is supplemented.
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
