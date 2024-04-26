from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from databaseConectionManager.databases.MySqlWrapperManager import MySqlWrapperManager

class MySqlManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManger: 
        return MySqlWrapperManager(connection)