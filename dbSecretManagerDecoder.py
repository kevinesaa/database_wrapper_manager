

def getSecretManagerObject(awsRegion:str, secretManagerArn:str) -> dict[str,any] :
    v : dict[str,any] = {"host":"localhot","port":3601, "filePath":"my_sqlite_db.sqlite","db_name":"users_db"}
    return v
