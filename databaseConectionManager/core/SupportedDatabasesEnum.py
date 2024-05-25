from enum import Enum, unique


@unique
class DatabaseType(Enum):
    MY_SQL = 1
    POSTGRE_SQL = 2
    SQLITE = 3
    MS_SQL_SERVER = 4
    
    '''this work with pyodbc. More info at: https://github.com/mkleehammer/pyodbc/wiki'''
    IBM_DB2_ODBC = 5 