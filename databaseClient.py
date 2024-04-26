
from databaseConectionManager.factory.SimpleFactory import DatabaseSimpleFactory
from databaseConectionManager.core.SupportedDatabasesEnum import DatabaseType
from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManger

import dbSecretManagerDecoder
import dbConectionCreator

# step 1
def getSecretManagerObject(awsRegion:str, secretManagerArn:str) -> dict[str,any] :
    return dbSecretManagerDecoder.getSecretManagerObject(awsRegion, secretManagerArn)

# step 2
def cretateDbConfig(secretManagerObject:dict[str,any]) -> dict[str,any]:
    return dbConectionCreator.cretateDbConfig(secretManagerObject)

# step 3
def createDbConnection(dbConfig) :
    return dbConectionCreator.createDbConnection(dbConfig)

if (__name__ == "__main__"):
    myRegion : str = "us-west-2" # change by AWS_REGION from environment
    mySecrectManagerArn : str = "" #set as environment
    mySecretObject = getSecretManagerObject(myRegion,mySecrectManagerArn)
    myDbConfig = cretateDbConfig(mySecretObject)
    myDbConectionObject = createDbConnection(myDbConfig)
    databaseManager : DatabaseWrapperManger = DatabaseSimpleFactory.createDatabaseManager(DatabaseType.SQLITE,myDbConectionObject)
    rows = databaseManager.getRows("SELECT * FROM users")
    