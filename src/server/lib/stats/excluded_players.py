from datetime import date
from lib.db.database_table import get_table
from lib.basketball.basketball_reference import get_top_players
import unicodedata
import config
import lib.stats.stats as stats
from util.date_util import get_today_pst, str_to_date

def get_excluded_players() -> list[str]:
    """Fetches list of excluded players if it does not exist in the db or has not been refreshed in 3 days"""
    excluded_players_table = get_table(config.SUPABASE_EXCLUDED_PLAYERS_TABLE, config.SUPABASE_SCHEMA)
    excluded_players_response = excluded_players_table.get_table().select('name,created_at').execute()
    if excluded_players_response:
        refresh_top_players = True
        if len(excluded_players_response.data) > 0:
            delta = get_today_pst() - str_to_date(excluded_players_response.data[0]['created_at'])
            refresh_top_players = delta.days > config.EXCLUDED_PLAYERS_REFRESH_DAYS
            
        if refresh_top_players:
            excluded_players_table.get_table().delete().neq('name', '').execute() # clear all data
            player_data = stats.get_top_players(config.ANALYSIS_DAYS, min_mp=config.TOP_PLAYERS_MIN_MP, min_fantasy_score=config.TOP_PLAYERS_MIN_FANTASY_SCORE)
            player_names = [player['player'] for player in player_data]
            excluded_players_table.insert([{ 'name': name } for name in player_names])
            return player_names
    
    return [row['name'] for row in excluded_players_response.data]

def __normalize(name: str) -> str:
    normalized_text = unicodedata.normalize('NFKD', name)
    ascii_text = "".join([c for c in normalized_text if not unicodedata.combining(c)])
    return ascii_text