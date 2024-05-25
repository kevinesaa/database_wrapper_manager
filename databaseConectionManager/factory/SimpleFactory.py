

from databaseConectionManager.factory.factories.DatabaseManagerFactory import DatabaseManagerFactory
from databaseConectionManager.factory.factories.MySqlManagerFactory import MySqlManagerFactory
from databaseConectionManager.factory.factories.PostgreSqlManagerFactory import PostgreSqlManagerFactory
from databaseConectionManager.factory.factories.SqliteManagerFactory import SqliteManagerFactory
from databaseConectionManager.factory.factories.MsSqlServerManagerFactory import MsSqlServerManagerFactory
from databaseConectionManager.factory.factories.IbmDb2OdbcManagerFactory import ImbDb2OdbcManagerFactory

from databaseConectionManager.core.SupportedDatabasesEnum import DatabaseType
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager


from typing import Dict



class DatabaseSimpleFactory:
    
    __databaseFactories : Dict[DatabaseType,DatabaseManagerFactory] = None

    def _initDatasesDict() -> None :
        if DatabaseSimpleFactory.__databaseFactories is None:
            DatabaseSimpleFactory.__databaseFactories = {}
            DatabaseSimpleFactory.__databaseFactories[DatabaseType.MY_SQL] = MySqlManagerFactory()
            DatabaseSimpleFactory.__databaseFactories[DatabaseType.POSTGRE_SQL] = PostgreSqlManagerFactory()
            DatabaseSimpleFactory.__databaseFactories[DatabaseType.SQLITE] = SqliteManagerFactory()
            DatabaseSimpleFactory.__databaseFactories[DatabaseType.MS_SQL_SERVER] = MsSqlServerManagerFactory()
            DatabaseSimpleFactory.__databaseFactories[DatabaseType.IBM_DB2_ODBC] = ImbDb2OdbcManagerFactory()

    
    def createDatabaseManager(databaseType:DatabaseType, connection) -> DatabaseWrapperManager:
       
        DatabaseSimpleFactory._initDatasesDict()
        factory : DatabaseManagerFactory = DatabaseSimpleFactory.__databaseFactories[databaseType]
        return factory.createDatabaseManager(connection)
        