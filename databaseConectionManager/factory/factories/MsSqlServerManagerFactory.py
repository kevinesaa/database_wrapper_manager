from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.databases.MsSqlServerWrapperManager import MsSqlServerWrapperManager

class MsSqlServerManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManager: 
        return MsSqlServerWrapperManager(connection)