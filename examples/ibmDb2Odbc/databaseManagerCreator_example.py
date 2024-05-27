
import pyodbc # replace this line with your specific database engine, example: import sqlite3

import json

from src import DatabaseWrapperManager


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


def createDatabseManager(awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    
    databaseSecretString = _getSecretManagerString(awsRegion, secretManagerArn)
    databaseSecretJson = json.loads(databaseSecretString)
    dbConection = _cretateDbConection(databaseSecretJson)
    
   
    return DatabaseWrapperManager(dbConection)
