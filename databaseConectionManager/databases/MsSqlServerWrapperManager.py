from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from typing import List


class MsSqlServerWrapperManager(DatabaseWrapperManger):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        #self.conection

    def getRows(self,quearyString:str,params=None) -> List:
        print("get rows from ms sql server")
        
    def executeQuery(self,quearyString:str,params=None) -> None :
        print("execuete from ms sql server")
        
    
    def closeConection(self) -> None:
        print("close conection from ms sql server")
        