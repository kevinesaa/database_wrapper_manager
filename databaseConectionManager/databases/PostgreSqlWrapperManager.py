#import psycopg2
#from psycopg2 import OperationalError
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager


class PostgreSqlWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        #self.conection
        pass

    def executeQuery(self,queryString:str,params:list=None) -> list[dict[str,object]]:
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
    
    def executeOneStatement(self,queryString:str,params=None) :
        print("execute query from my postgre")
        
    def executeBulkStatement(self,queryString:str,params=None) -> None:
        pass
    
    def closeConection(self) -> None:
        print("execute query from my postgre")
        