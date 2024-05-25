#import psycopg2
#from psycopg2 import OperationalError
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from typing import List

class PostgreSqlWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        #self.conection
        pass

    def getRows(self,queryString:str,params=None) -> List:
        '''
        cursor = self.connection.cursor()
        try:
            
            cursor.execute(queryString)
            
            return cursor.fetchall()
        except OperationalError as e:
            print(f"The error '{e}' occurred")
            raise
        '''
        print("get rows from my postgre")
    
    def executeQuery(self,queryString:str,params=None) -> None :
        print("execute query from my postgre")
        
    
    def closeConection(self) -> None:
        print("execute query from my postgre")
        