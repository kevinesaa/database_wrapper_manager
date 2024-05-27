from src.SqlCommandExecutor import SqlCommandExecutor
from src.IDatabaseManager import IDatabaseManager
from src.ITransaction import ITransaction

class TransactionWrapper(ITransaction):
    
    def __init__(self, dbManager:IDatabaseManager,id:str) :
        super().__init__(self,dbManager,id)
        self.dbManager = dbManager
        self._cursor = dbManager.connection.cursor()
        self._id = id
    
    def _finishTransaction(self) -> None:
        self._cursor.close()
        self.dbManager.removeTransactionRegister(self._id)
        self._cursor = None
        self.dbManager = None
        del self._cursor
    
    def commit(self) -> None:
        self.dbManager.connection.commit()
        self._finishTransaction()
    
    def rollback(self) -> None:
        self.dbManager.connection.rollback()
        self._finishTransaction()
    
    def executeQuery(self,queryString:str,params:list[tuple]=None) -> list[dict[str,object]]:
        cursor = self._cursor
        return SqlCommandExecutor.executeQuery(cursor,queryString,params)
    
    def executeOneStatement(self,queryString:str,params:tuple=None) -> int:
        cursor = self._cursor
        return SqlCommandExecutor.executeOneStatement(cursor,queryString,params)
    
    def executeBulkStatement(self,queryString:str,params:list[tuple]=None) -> None:
        cursor = self._cursor
        SqlCommandExecutor.executeBulkStatement(cursor,queryString,params)
        
