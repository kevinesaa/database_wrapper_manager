from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from typing import List




class IbmDb2OdbcWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        

    def getRows(self,queryString:str,params=None) -> List:
        print("get rows from ibm Db2")
        
    def executeQuery(self,queryString:str,params=None) -> None :
        print("execuete from ibm Db2")
        
    
    def closeConection(self) -> None:
        print("close conection from ibm Db2")
        