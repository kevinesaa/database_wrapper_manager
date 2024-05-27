from abc import ABC, abstractmethod
from src.IDatabaseManager import IDatabaseManager

class ITransaction(ABC):
    
    def __init__(self,dbManager:IDatabaseManager,id:str):
        pass