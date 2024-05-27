from abc import ABC
from . import IDatabaseManager

class ITransaction(ABC):
    
    def __init__(self,dbManager:IDatabaseManager,id:str):
        pass