from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.databases.IbmDb2OdbcWrapperManager import IbmDb2OdbcWrapperManager

class ImbDb2OdbcManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManager: 
        return IbmDb2OdbcWrapperManager(connection)