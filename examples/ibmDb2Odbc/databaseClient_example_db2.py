

from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.core.SupportedDatabasesEnum import DatabaseType

from examples.ibmDb2Odbc import databaseManagerCreator_example


def createDatabaseManager(dbType: DatabaseType, awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    return databaseManagerCreator_example.createDatabseManager(dbType,awsRegion, secretManagerArn)



def excuteCliente(event={}, context={}):
    
    # this is a example with a ODBC IBM i access DB2 data base
    
    myRegion : str = "us-west-2" # change by os.environ['AWS_REGION']
    mySecrectManagerArn : str = "" #set as environment
    databaseManager : DatabaseWrapperManager = createDatabaseManager(DatabaseType.IBM_DB2_ODBC, myRegion, mySecrectManagerArn)
    rows : list[dict[str,object]] = databaseManager.executeQuery("SELECT * FROM users")
    for r in rows:
        print(r)
    databaseManager.closeConection()

    return {}
    