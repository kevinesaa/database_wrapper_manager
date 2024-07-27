import mysql.connector
import json

from src import DatabaseWrapperManager


def _getSecretManagerString(awsRegion:str, secretManagerArn:str) -> str :
    
    # here make your logic to get the secret str with boto3
    secret : str ='''
        {
            "db_host":"localhost",
            "db_name":"example",
            "db_user":"admin",
            "db_pass":"12345678"
        }
        '''
    secret = " ".join([ line.strip() for line in secret.splitlines()])
    secret = secret.strip()
    return secret



def _cretateDbConnection(secretManagerJsonObject:dict[str,object]) -> object:
    
    # here add the logic to create a specific database connection
    
    return  mysql.connector.connect(
        host = secretManagerJsonObject["db_host"],
        user = secretManagerJsonObject["db_user"],
        passwd  = secretManagerJsonObject["db_pass"],
        database = secretManagerJsonObject["db_name"]
    )  
    


def createDatabaseManager(awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    databaseSecretString = _getSecretManagerString(awsRegion, secretManagerArn)
    databaseSecretJson = json.loads(databaseSecretString)
    dbConection = _cretateDbConnection(databaseSecretJson)
    
    return DatabaseWrapperManager(dbConection)
