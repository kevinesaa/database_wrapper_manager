from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger
from databaseConectionManager.databases.IbmDb2WrapperManager import IbmDb2WrapperManager

class ImbDb2ManagerFactory(DatabaseManagerFactory):
    
    def createDatabaseManager(self, connection) -> DatabaseWrapperManger: 
        return IbmDb2WrapperManager(connection)