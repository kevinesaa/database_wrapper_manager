from abc import ABC, abstractmethod
from datetime import datetime

class DatabaseWrapperManager(ABC) :

    def __init__(self, dbConnection) :
        self.__connection = dbConnection
    
    def convertToJsonSerializable(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
    
    @property
    def connection(self) :
        return self.__connection

    @abstractmethod
    def executeQuery(self,queryString:str,params:list=None) -> list[dict[str,object]]:
        pass
    
    @abstractmethod
    def executeOneStatement(self,queryString:str,params=None) :
        pass
    
    @abstractmethod
    def executeBulkStatement(self,queryString:str,params=None) -> None:
        pass
   
    @abstractmethod
    def closeConection(self) -> None:
        pass