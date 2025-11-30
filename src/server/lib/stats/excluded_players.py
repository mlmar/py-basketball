from lib.db.database_table import DatabaseTable
from lib.basketball.basketball_reference import get_all_stars
import config

excluded_players_table = DatabaseTable(config.SUPABASE_EXCLUDED_PLAYERS_TABLE)
def get_excluded_players() -> list[str]:
    """Fetches list of excluded players if it does not exist in the db"""
    excluded_players_response = excluded_players_table.get_table().select('name').execute()
    if excluded_players_response.data is None or len(excluded_players_response.data) == 0:
        player_names = get_all_stars()
        excluded_players_table.insert([{ 'name': name } for name in player_names])
        return player_names
    
    return [row['name'] for row in excluded_players_response.data]