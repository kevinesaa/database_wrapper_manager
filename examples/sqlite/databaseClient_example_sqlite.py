

from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.core.SupportedDatabasesEnum import DatabaseType

from examples.sqlite import databaseManagerCreator_example


def createDatabaseManager(dbType: DatabaseType, awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    return databaseManagerCreator_example.createDatabseManager(dbType,awsRegion, secretManagerArn)



def excuteCliente(event={}, context={}):
    
    
    myRegion : str = "us-west-2" # change by os.environ['AWS_REGION']
    mySecrectManagerArn : str = "" #set as environment
    databaseManager : DatabaseWrapperManager = createDatabaseManager(DatabaseType.SQLITE, myRegion, mySecrectManagerArn)
    databaseManager.executeOneStatement("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    databaseManager.executeOneStatement("INSERT INTO users (name) VALUES ('mario')")
    rows : list[dict[str,object]] = databaseManager.executeQuery("SELECT * FROM users")
    for r in rows:
        print(r)
    databaseManager.closeConection()

    return {}
    