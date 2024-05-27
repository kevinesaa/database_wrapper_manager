

from src import DatabaseWrapperManager

from examples.ibmDb2Odbc import databaseManagerCreator_example


def createDatabaseManager(awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    return databaseManagerCreator_example.createDatabseManager(awsRegion, secretManagerArn)



def excuteCliente(event={}, context={}):
    
    myRegion : str = "us-west-2" # change by os.environ['AWS_REGION']
    mySecrectManagerArn : str = "" #set as environment
    databaseManager : DatabaseWrapperManager = createDatabaseManager(myRegion, mySecrectManagerArn)
    rows : list[dict[str,object]] = databaseManager.executeQuery("SELECT * FROM users")
    for r in rows:
        print(r)
    databaseManager.closeConection()

    return {}
    