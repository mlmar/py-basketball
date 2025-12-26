from postgrest import SyncRequestBuilder
from lib.db.client import get_client
        
__tables = {} # cache table connections
def get_table(table_name: str, schema: str = None) -> SyncRequestBuilder:
    """Gets cached table connections"""
    key = f'{table_name}_{schema}'
    global __tables
    if key not in __tables:
        client = get_client()
        if schema:
            __tables[key] = client.schema(schema).table(table_name)
        else:
            __tables[key] = client.table(table_name)
    
    return __tables[key]