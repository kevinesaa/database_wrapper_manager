from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager



class MsSqlServerWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        #self.conection

    def executeQuery(self,queryString:str,params:list=None) -> list[dict[str,object]]:
        print("get rows from ms sql server")
        
    def executeOneStatement(self,queryString:str,params=None) :
        print("execuete from ms sql server")
        
    def executeBulkStatement(self,queryString:str,params=None) -> None:
        pass
    
    def closeConection(self) -> None:
        print("close conection from ms sql server")
        