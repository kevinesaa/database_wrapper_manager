

from src import DatabaseWrapperManager
from examples.sqlite import databaseManagerCreator_example 


def createDatabaseManager(awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    return databaseManagerCreator_example.createDatabseManager(awsRegion, secretManagerArn)



def excuteCliente(event={}, context={}):
    
    
    myRegion : str = "us-west-2" # change by os.environ['AWS_REGION']
    mySecrectManagerArn : str = "" #set as environment
    databaseManager : DatabaseWrapperManager = createDatabaseManager(myRegion, mySecrectManagerArn)
    databaseManager.executeOneStatement("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    rows : list[dict[str,object]] = databaseManager.executeStatmentWithReturn("INSERT INTO users (name) VALUES ('mario') RETURNING *")
    
    print("before")
    for r in rows:
        print(r)
    
    print("")
    print("after")
    rows = databaseManager.executeQuery("SELECT * FROM users")
    for r in rows:
        print(r)
    databaseManager.closeConnection()

    return {}
    