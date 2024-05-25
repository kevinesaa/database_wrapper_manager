from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from typing import List




class IbmDb2WrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        

    def getRows(self,quearyString:str,params=None) -> List:
        print("get rows from ibm Db2")
        
    def executeQuery(self,quearyString:str,params=None) -> None :
        print("execuete from ibm Db2")
        
    
    def closeConection(self) -> None:
        print("close conection from ibm Db2")
        