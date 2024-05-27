from abc import ABC, abstractmethod
from IDatabaseManager import IDatabaseManager

class ITransaction(ABC):
    
    def __init__(self,dbManager:IDatabaseManager,id:str):
        pass