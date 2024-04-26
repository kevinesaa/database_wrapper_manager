from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from databaseConectionManager.databases.PostgreSqlWrapperManager import PostgreSqlWrapperManager

class  PostgreSqlManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManger: 
        return PostgreSqlWrapperManager(connection)