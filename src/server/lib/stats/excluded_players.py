from lib.db.database_table import DatabaseTable
from lib.basketball.basketball_reference import get_top_players
import unicodedata
import config

excluded_players_table = DatabaseTable(config.SUPABASE_EXCLUDED_PLAYERS_TABLE)
def get_excluded_players() -> list[str]:
    """Fetches list of excluded players if it does not exist in the db"""
    excluded_players_response = excluded_players_table.get_table().select('name').execute()
    if excluded_players_response.data is None or len(excluded_players_response.data) == 0:
        player_names = get_top_players()
        excluded_players_table.insert([{ 'name': __normalize(name) } for name in player_names])
        return player_names
    
    return [row['name'] for row in excluded_players_response.data]

def __normalize(name: str) -> str:
    normalized_text = unicodedata.normalize('NFKD', name)
    ascii_text = "".join([c for c in normalized_text if not unicodedata.combining(c)])
    return ascii_text