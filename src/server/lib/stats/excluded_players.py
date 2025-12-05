from datetime import date
from lib.db.database_table import DatabaseTable
from lib.basketball.basketball_reference import get_top_players
import unicodedata
import config

excluded_players_table = DatabaseTable(config.SUPABASE_EXCLUDED_PLAYERS_TABLE)
def get_excluded_players() -> list[str]:
    """Fetches list of excluded players if it does not exist in the db or has not been refreshed in 3 days"""
    excluded_players_response = excluded_players_table.get_table().select('name,created_at').execute()
    if excluded_players_response:
        refresh_top_players = True
        if len(excluded_players_response.data) > 0:
            delta = date.today() - __str_to_date(excluded_players_response.data[0]['created_at'])
            refresh_top_players = delta.days > 3
            
        if refresh_top_players:
            player_names = get_top_players()
            excluded_players_table.insert([{ 'name': __normalize(name) } for name in player_names])
            return player_names
    
    return [row['name'] for row in excluded_players_response.data]

def __normalize(name: str) -> str:
    normalized_text = unicodedata.normalize('NFKD', name)
    ascii_text = "".join([c for c in normalized_text if not unicodedata.combining(c)])
    return ascii_text

def __str_to_date(date_str: str) -> date:
    """Converts date str YYYY-MM-DDTimestamp to date"""
    date_str_arr = date_str.split('T')
    y, m, d = date_str_arr[0].split('-')
    return date(int(y), int(m), int(d))