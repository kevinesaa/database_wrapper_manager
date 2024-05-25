from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.databases.IbmDb2WrapperManager import IbmDb2WrapperManager

class ImbDb2ManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManager: 
        return IbmDb2WrapperManager(connection)