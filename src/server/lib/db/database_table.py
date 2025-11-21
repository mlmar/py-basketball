from lib.db.client import get_client
from lib.basketball.player import Player

class DatabaseTable():
    """ Class for connecting to Supabase Table and performing modifications """
    table_name: str = None
    table = None

    def __init__(self, table_name: str):
        self.table_name = table_name
        
        client = get_client()
        self.table = client.table(self.table_name)

    def insert_players(self, players: list[Player]):
        print(f'Inserting {len(players)} players to {self.table_name}')
        table_objects: list[dict] = [player.to_dict() for player in players]
        self.table.upsert(table_objects).execute()
        print(f'Successfully inserted players to {self.table_name}')