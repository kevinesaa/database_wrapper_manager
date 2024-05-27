from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.core.DatabaseWrapperManager import SqlCommand
from databaseConectionManager.core.DatabaseWrapperManager import TransactionWrapper

from datetime import datetime

class _MsSqlServerSqlCommand(SqlCommand):

    
    def executeQuery(cursor,queryString:str,params:list=None) -> list[dict[str,object]]:
        
        if (params is None):
            cursor.execute(queryString)
        else:
            cursor.execute(queryString,params)
        
        result = []
        for row in cursor.fetchall():
            result.append({column[0]: SqlCommand.convertToJsonSerializable(value) 
                           for column, value in zip(cursor.description, row)})
        
        return result
    
    def executeOneStatement(cursor,queryString:str,params:tuple=None) -> int:
        
        rowsCount = -1
        if (params is None):
            rowsCount = cursor.execute(queryString).rowcount
        else:
            rowsCount = cursor.execute(queryString,params).rowcount
        
        return rowsCount
    
    
    def executeBulkStatement(cursor,queryString:str,params:list[tuple]=None) -> None:
        
        if (params is None):
            cursor.executemany(queryString)
        else:
            cursor.executemany(queryString,params)

class _MsSqlServerTransactionWrapper(TransactionWrapper):
    
    def __init__(self, dbManager,id) :
        super().__init__(self,dbManager)
        self._cursor = dbManager.connection.cursor()
        self._id = id
    
    def _finishTransaction(self) -> None:
        self._cursor.close()
        self.dbManager.removeTransactionRegister(self._id)
        self._cursor = None
        self.dbManager = None
    
    def commit(self) -> None:
        self.dbManager.connection.commit()
        self._finishTransaction()
    
    def rollback(self) -> None:
        self.dbManager.connection.rollback()
        self._finishTransaction()
    
    def executeQuery(self,queryString:str,params:list[tuple]=None) -> list[dict[str,object]]:
        cursor = self._cursor
        return _MsSqlServerSqlCommand.executeQuery(cursor,queryString,params)
    
    def executeOneStatement(self,queryString:str,params:tuple=None) -> int:
        cursor = self._cursor
        return _MsSqlServerSqlCommand.executeOneStatement(cursor,queryString,params)
    
    def executeBulkStatement(self,queryString:str,params:list[tuple]=None) -> None:
        cursor = self._cursor
        _MsSqlServerSqlCommand.executeBulkStatement(cursor,queryString,params)
        

class MsSqlServerWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        self._transactionInProgress = []
        
    def executeQuery(self,queryString:str,params:list[tuple]=None) -> list[dict[str,object]]:
        
        self._raiseOnTransactionInProgress()
        
        cursor = self.connection.cursor()
        result = _MsSqlServerSqlCommand.executeQuery(cursor,queryString,params)
        cursor.close()
        return result
        
    def executeOneStatement(self,queryString:str,params:tuple=None) -> int:
        self._raiseOnTransactionInProgress()
        
        cursor = self.connection.cursor()
        result = _MsSqlServerSqlCommand.executeOneStatement(cursor,queryString,params)
        self.connection.commit()
        cursor.close()
        return result
        
    def executeBulkStatement(self,queryString:str,params:list[tuple]=None) -> None:
        self._raiseOnTransactionInProgress()
        
        cursor = self.connection.cursor()
        _MsSqlServerSqlCommand.executeBulkStatement(cursor,queryString,params)
        self.connection.commit()
        cursor.close()


    def startTransaction(self) -> TransactionWrapper:
        id = datetime.now().strftime('%Y%m%d%H%M%S')
        self._transactionInProgress.append(id)
        return _MsSqlServerTransactionWrapper(self,id)        
    
    def closeConection(self) -> None:
        self.connection.close()
        
    def removeTransactionRegister(self, id) -> None :
        self._transactionInProgress = [ i for i in self._transactionInProgress if i != id]
    
    def _raiseOnTransactionInProgress(self):
        if(len(self._transactionInProgress) > 0):
            raise Exception("commit o rollback all pending transaction before execute a new query from manager")
