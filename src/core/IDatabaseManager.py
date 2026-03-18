from abc import ABC, abstractmethod


class IDatabaseManager(ABC):
    
    def __init__(self, dbConnection) :
        self.__connection = dbConnection

    @property
    def connection(self) :
        return self.__connection
    
    @abstractmethod
    def removeTransactionRegister(self, id) -> None :
        pass