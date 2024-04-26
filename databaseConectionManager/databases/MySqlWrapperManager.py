#import pymysql

from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from typing import List


class MySqlWrapperManager(DatabaseWrapperManger):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        #self.conection

    def getRows(self,quearyString:str,params=None) -> List:
        print("get rows from my sql")
        
    def executeQuery(self,quearyString:str,params=None) -> None :
        print("execuete from my sql")
        
    
    def closeConection(self) -> None:
        print("close conection from my sql")
        