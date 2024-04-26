import sqlite3



# step 2
def cretateDbConfig(secretManagerObject:dict[str,any]) -> dict[str,any]:
    #v : dict[str,any] = {"host":"localhot","port":3601, "filePath":"my_sqlite_db.sqlite","db_name":"users_db"}
    dbConfig = {
        "server":secretManagerObject["host"],
        "file":secretManagerObject["filePath"],
        "name":secretManagerObject["db_name"],
        "port":secretManagerObject["port"]
    }
    return dbConfig

# step 3
def createDbConnection(dbConfig:dict[str,any]) :
    
    pass
