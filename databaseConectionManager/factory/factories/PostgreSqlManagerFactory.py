from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.databases.PostgreSqlWrapperManager import PostgreSqlWrapperManager

class  PostgreSqlManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManager: 
        return PostgreSqlWrapperManager(connection)