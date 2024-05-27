from abc import ABC, abstractmethod


class IDatabaseManager(ABC):
    
    def __init__(self,dbConection) :
        self.__connection = dbConection

    @property
    def connection(self) :
        return self.__connection
    
    @abstractmethod
    def removeTransactionRegister(self, id) -> None :
        pass