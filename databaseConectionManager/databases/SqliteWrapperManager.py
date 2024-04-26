from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from typing import List


class SqliteWrapperManager(DatabaseWrapperManger):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        

    def getRows(self,quearyString:str,params=None) -> List:
        print("get rows from sqlite")
        
    def executeQuery(self,quearyString:str,params=None) -> None :
        print("execuete from sqlite")
        
    
    def closeConection(self) -> None:
        print("close conection from sqlite")
        