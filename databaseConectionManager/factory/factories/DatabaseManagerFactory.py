from abc import ABC, abstractmethod
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager

class DatabaseManagerFactory(ABC) :

    @abstractmethod
    def createDatabaseManager(self, connection) -> DatabaseWrapperManager: 
        pass