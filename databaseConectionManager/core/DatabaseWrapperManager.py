from abc import ABC, abstractmethod
from typing import List

class DatabaseWrapperManager(ABC) :

    def __init__(self, dbConnection) :
        self.__connection = dbConnection
    
    @property
    def connection(self) :
        return self.__connection

    @abstractmethod
    def getRows(self,queryString:str,params=None) -> List:
        pass
    
    @abstractmethod
    def executeQuery(self,queryString:str,params=None) -> None :
        pass
    
   
    @abstractmethod
    def closeConection(self) -> None:
        pass