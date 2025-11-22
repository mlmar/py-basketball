from lib.db.client import get_client

class DatabaseTable[T]():
    """Class for connecting to Supabase Table and performing modifications"""
    table_name: str = None
    table = None

    def __init__(self, table_name: str):
        self.table_name = table_name
        
        client = get_client()
        self.table = client.table(self.table_name)

    def get_table(self):
        return self.table

    def insert(self, items: list[T] | T):
        """Inserts a list of items or a single item to the table"""
        try:
            if isinstance(items, list):
                print(f'Inserting {len(items)} items to {self.table_name}')
                self.table.upsert(items).execute()
                print(f'Successfully inserted {len(items)} items to {self.table_name}')
            else:
                print(f'Inserting 1 item to {self.table_name}')
                self.table.upsert(items).execute()
                print(f'Successfully inserted 1 item to {self.table_name}')
        except:
            raise Exception(f'Failed to insert items to {self.table_name}')