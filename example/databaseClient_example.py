

from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.core.SupportedDatabasesEnum import DatabaseType

from example import databaseManagerCreator_example


def createDatabaseManager(dbType: DatabaseType, awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    pass
    #return databaseManagerCreator_example.getSecretManagerObject(awsRegion, secretManagerArn)



def excuteCliente(event={}, context={}):
    
    # this is a example with a ODBC IBM i access DB2 data base
    
    myRegion : str = "us-west-2" # change by os.environ['AWS_REGION']
    mySecrectManagerArn : str = "" #set as environment
    databaseManager : DatabaseWrapperManager =  createDatabaseManager(DatabaseType.SQLITE, myRegion, mySecrectManagerArn)
    rows : list[dict[str,object]] = databaseManager.getRows("SELECT * FROM users")
    databaseManager.closeConection()

    return {}
    