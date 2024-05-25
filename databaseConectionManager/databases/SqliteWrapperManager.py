from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from typing import List


class SqliteWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        

    def getRows(self,queryString:str,params=None) -> List:
        print("get rows from sqlite")
        
    def executeQuery(self,queryString:str,params=None) -> None :
        print("execuete from sqlite")
        
    
    def closeConection(self) -> None:
        print("close conection from sqlite")
        