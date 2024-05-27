from datetime import datetime
from src.SqlCommandExecutor import SqlCommandExecutor
from src.TransactionWrapper import TransactionWrapper
from src.IDatabaseManager import IDatabaseManager


class DatabaseWrapperManager(IDatabaseManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        dbConnection.autocommit = False
        self._transactionInProgress = []
        
    def executeQuery(self,queryString:str,params:list[tuple]=None) -> list[dict[str,object]]:
        
        self._raiseOnTransactionInProgress()
        
        cursor = self.connection.cursor()
        result = SqlCommandExecutor.executeQuery(cursor,queryString,params)
        cursor.close()
        del cursor
        return result
        
    def executeOneStatement(self,queryString:str,params:tuple=None) -> int:
        self._raiseOnTransactionInProgress()
        
        cursor = self.connection.cursor()
        result = SqlCommandExecutor.executeOneStatement(cursor,queryString,params)
        self.connection.commit()
        cursor.close()
        del cursor
        return result
        
    def executeBulkStatement(self,queryString:str,params:list[tuple]=None) -> None:
        self._raiseOnTransactionInProgress()
        
        cursor = self.connection.cursor()
        SqlCommandExecutor.executeBulkStatement(cursor,queryString,params)
        self.connection.commit()
        cursor.close()
        del cursor

    def startTransaction(self) -> TransactionWrapper:
        id = datetime.now().strftime('%Y%m%d%H%M%S%f')
        self._transactionInProgress.append(id)
        return TransactionWrapper(self,id)        
    
    def removeTransactionRegister(self, id) -> None :
        self._transactionInProgress = [ i for i in self._transactionInProgress if i != id]
    
    def _raiseOnTransactionInProgress(self):
        if(len(self._transactionInProgress) > 0):
            raise Exception("commit o rollback all pending transaction before execute a new query from manager")
    
    def closeConection(self) -> None:
        self.connection.close()