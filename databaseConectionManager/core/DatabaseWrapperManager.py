from abc import ABC, abstractmethod
from datetime import datetime

class SqlCommand(ABC):

    def convertToJsonSerializable(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
    
    @abstractmethod
    def executeQuery(cursor,queryString:str,params:list=None) -> list[dict[str,object]]:
        pass
    
    @abstractmethod
    def executeOneStatement(cursor,queryString:str,params=None) -> int:
        pass
    
    @abstractmethod
    def executeBulkStatement(cursor,queryString:str,params=None) -> None:
        pass
class TransactionWrapper(ABC):
    
    def __init__(self,dbManager) :
        self.__dbManager = dbManager
    
    @property
    def dbManager(self) :
        return self.__dbManager

    @property
    def dbManager(self,manager) :
        self.__dbManager = manager

    @abstractmethod
    def commit(self) -> None:
        pass
    @abstractmethod
    def rollback(self) -> None:
        pass
    @abstractmethod
    def executeQuery(self,queryString:str,params:list[tuple]=None) -> list[dict[str,object]]:
        pass
    @abstractmethod
    def executeOneStatement(self,queryString:str,params:tuple=None) -> int:
        pass
    @abstractmethod
    def executeBulkStatement(self,queryString:str,params:list[tuple]=None) -> None:
        pass

class DatabaseWrapperManager(ABC) :

    def __init__(self, dbConnection) :
        self.__connection = dbConnection
    

    @property
    def connection(self) :
        return self.__connection

    @abstractmethod
    def executeQuery(self,queryString:str,params:list=None) -> list[dict[str,object]]:
        pass
    
    @abstractmethod
    def executeOneStatement(self,queryString:str,params=None) -> int :
        pass
    
    @abstractmethod
    def executeBulkStatement(self,queryString:str,params=None) -> None:
        pass
   
    @abstractmethod
    def closeConection(self) -> None:
        pass
    
    @abstractmethod
    def startTransaction(self) -> TransactionWrapper:
        pass