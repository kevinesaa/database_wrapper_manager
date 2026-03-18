

from src import DatabaseWrapperManager
from examples.sqlite import databaseManagerCreator_example 


def createDatabaseManager(awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    return databaseManagerCreator_example.createDatabaseManager(awsRegion, secretManagerArn)



def executeClient(event={}, context={}):

    myRegion: str = "us-west-2"  # change by os.environ['AWS_REGION']
    mySecretManagerArn: str = ""  # set as environment
    databaseManager: DatabaseWrapperManager = createDatabaseManager(myRegion, mySecretManagerArn)
    databaseManager.executeOneStatement("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    databaseManager.executeOneStatement("DELETE FROM users")

    print("")
    print("after delete")
    rows = databaseManager.executeQuery("SELECT * FROM users")
    for r in rows:
        print(r)
    
    print("")
    rows : list[dict[str,object]] = databaseManager.executeStatementWithReturning("INSERT INTO users (name) VALUES ('mario') RETURNING *")
    print("before")
    for r in rows:
        print(r)
    
    print("")
    print("after")
    rows = databaseManager.executeQuery("SELECT * FROM users")
    for r in rows:
        print(r)

    transaction = databaseManager.startTransaction()
    try:
        transaction.executeQuery("INSERT INTO users (name) VALUES ('luigi')")
        transaction.executeQuery("INSERT INTO users (name) VALUES ('peach')")
        transaction.commit()
    except Exception as exception:
        transaction.rollback()
        print(exception)
    
    print("")
    print("after transaction")
    rows = databaseManager.executeQuery("SELECT * FROM users")
    for r in rows:
        print(r)
    
    databaseManager.closeConnection()

    return {}
    