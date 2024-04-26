from abc import ABC, abstractmethod
from typing import List

class DatabaseWrapperManger(ABC) :

    def __init__(self, dbConnection) :
        self.__connection = dbConnection
    
    @property
    def connection(self) :
        return self.__connection

    @abstractmethod
    def getRows(self,quearyString:str,params=None) -> List:
        pass
    
    @abstractmethod
    def executeQuery(self,quearyString:str,params=None) -> None :
        pass
    
   
    @abstractmethod
    def closeConection(self) -> None:
        pass