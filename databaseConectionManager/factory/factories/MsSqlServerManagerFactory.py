from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from databaseConectionManager.databases.MsSqlServerWrapperManager import MsSqlServerWrapperManager

class MsSqlServerManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManger: 
        return MsSqlServerWrapperManager(connection)