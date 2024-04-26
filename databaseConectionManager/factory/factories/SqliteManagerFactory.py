from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from databaseConectionManager.databases.SqliteWrapperManager import SqliteWrapperManager

class SqliteManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManger: 
        return SqliteWrapperManager(connection)