from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager

# https://code.google.com/archive/p/pyodbc/wikis/Features.wiki
# https://github.com/mkleehammer/pyodbc/wiki 
#import pyodbc



class IbmDb2OdbcWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        

    def executeQuery(self,queryString:str,params:list=None) -> list[dict[str,object]]:
        print("get rows from ibm Db2")
        
    def executeOneStatement(self,queryString:str,params=None) :
        print("execuete from ibm Db2")
        
    def executeBulkStatement(self,queryString:str,params=None) -> None:
        pass
        
    def closeConection(self) -> None:
        print("close conection from ibm Db2")
        