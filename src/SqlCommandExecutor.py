from datetime import datetime


class SqlCommandExecutor():

    def convertToJsonSerializable(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
    
    def executeQuery(cursor,queryString:str,params:list=None) -> list[dict[str,object]]:
        
        if (params is None):
            cursor.execute(queryString)
        else:
            cursor.execute(queryString,params)
        
        result = []
        
        for row in cursor.fetchall():
            result.append({column[0]: SqlCommandExecutor.convertToJsonSerializable(value) 
                           for column, value in zip(cursor.description, row)})
        return result
    
    def executeOneStatement(cursor,queryString:str,params:tuple=None) -> int:
        
        rowsCount = -1
        if (params is None):
            rowsCount = cursor.execute(queryString).rowcount
        else:
            rowsCount = cursor.execute(queryString,params).rowcount
        
        return rowsCount
    
    
    def executeBulkStatement(cursor,queryString:str,params:list[tuple]=None) -> None:
        
        if (params is None):
            cursor.executemany(queryString)
        else:
            cursor.executemany(queryString,params)

