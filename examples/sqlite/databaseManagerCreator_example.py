
import sqlite3 # replace this line with your specific database engine, example: import pyodbc 

import json

from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.factory.SimpleFactory import DatabaseSimpleFactory
from databaseConectionManager.core.SupportedDatabasesEnum import DatabaseType



def _getSecretManagerString(awsRegion:str, secretManagerArn:str) -> str :
    
    # here make your logic to get the secret str with boto3
    # a trip could be add the dbType value to the secret manager
    secret : str ='''
        {
            "db_type": "IBM_DB2_ODBC",
            "db_host":"localhost",
            "db_name":"example",
            "db_user":"admin",
            "db_pass":"12345678"
        }
        '''
    secret = " ".join([ line.strip() for line in secret.splitlines()])
    secret = secret.strip()
    return secret



def _cretateDbConection(secretManagerJsonObject:dict[str,object]) -> object:
    
    # here add the logic to create a specific database connection

    # this is a example from a IBM i access DB2 data base
    # https://www.ibm.com/docs/en/i/7.4?topic=details-connection-string-keywords
    dbConfib= {
        "DRIVER": "IBM i Access ODBC Driver",
        "SYSTEM": secretManagerJsonObject["db_host"],
        "DATABASE": secretManagerJsonObject["db_name"],
        "UID": secretManagerJsonObject["db_user"],
        "PWD": secretManagerJsonObject["db_pass"],
    } 

    connectionString = ";".join(
        f"{k}={v}" for k, v in dbConfib.items()
    )

    return pyodbc.connect(connectionString)


def createDatabseManager(dbType: DatabaseType, awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    # a trip could be add the dbType value to the secret manager
    databaseSecretString = _getSecretManagerString(awsRegion, secretManagerArn)
    databaseSecretJson = json.loads(databaseSecretString)
    dbConection = _cretateDbConection(databaseSecretJson)
    
    # with the trip the return looks something like
    # dbTypeName = databaseSecretJson['db_type']
    # dbType = DatabaseType[dbTypeName]
    # return DatabaseSimpleFactory.createDatabaseManager(dbType,dbConection)
    
    return DatabaseSimpleFactory.createDatabaseManager(dbType,dbConection)
