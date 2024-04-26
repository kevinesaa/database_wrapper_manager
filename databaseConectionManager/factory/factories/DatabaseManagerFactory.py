from abc import ABC, abstractmethod
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger

class DatabaseManagerFactory(ABC) :

    @abstractmethod
    def createDatabaseManager(self, connection) -> DatabaseWrapperManger: 
        pass