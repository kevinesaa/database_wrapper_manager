
import sqlite3 # replace this line with your specific database engine, example: import pyodbc 

import json

from src import DatabaseWrapperManager




def _getSecretManagerString(awsRegion:str, secretManagerArn:str) -> str :
    
    # here make your logic to get the secret str with boto3
    # a trip could be add the dbType value to the secret manager
    secret : str ='''
        {
            "db_path":"users.db"
        }
        '''
    secret = " ".join([ line.strip() for line in secret.splitlines()])
    secret = secret.strip()
    return secret



def _cretateDbConection(secretManagerJsonObject:dict[str,object]) -> object:
    
    return sqlite3.connect(secretManagerJsonObject["db_path"])


def createDatabseManager(awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    # a trip could be add the dbType value to the secret manager
    databaseSecretString = _getSecretManagerString(awsRegion, secretManagerArn)
    databaseSecretJson = json.loads(databaseSecretString)
    dbConection = _cretateDbConection(databaseSecretJson)
    
    return DatabaseWrapperManager(dbConection)
