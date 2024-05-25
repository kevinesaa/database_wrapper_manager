from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.core.DatabaseWrapperManager import SqlCommand
from databaseConectionManager.core.DatabaseWrapperManager import TransactionWrapper


class MySqlWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        #self.conection

    def executeQuery(self,queryString:str,params:list=None) -> list[dict[str,object]]:
        print("get rows from my sql")
        
    def executeOneStatement(self,queryString:str,params=None) :
        print("execuete from my sql")
        
    def executeBulkStatement(self,queryString:str,params=None) -> None:
        pass
    
    def startTransaction(self) -> TransactionWrapper:
        pass
    
    def closeConection(self) -> None:
        print("close conection from my sql")
        