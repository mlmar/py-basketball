"""Exposing env variables as config props"""

import os
from dotenv import load_dotenv

load_dotenv()
DEV: str = os.environ.get('DEV')
CLIENT_URL: str = os.environ.get('VITE_CLIENT_URL')
SERVER_URL: str = os.environ.get('VITE_SERVER_URL')
SUPABASE_URL: str = os.environ.get('SUPABASE_URL')
SUPABASE_KEY: str = os.environ.get('SUPABASE_KEY')
SUPABASE_JWT_SECRET: str = os.environ.get('SUPABASE_JWT_SECRET')
SUPABASE_SAVED_DATES_TABLE: str = 'saved_dates'
SUPABASE_PLAYER_DATA_TABLE: str = 'player_data'
SUPABASE_PROJECTED_ANALYSIS_STATUS_TABLE: str = 'projected_analysis_status'
SUPABASE_PROJECTED_ANALYSIS_DATA_TABLE: str = 'projected_analysis_data'
SUPABASE_TRENDING_ANALYSIS_STATUS_TABLE: str = 'trending_analysis_status'
SUPABASE_TRENDING_ANALYSIS_DATA_TABLE: str = 'trending_analysis_data'
SUPABASE_EXCLUDED_PLAYERS_TABLE: str = 'excluded_players'

ANALYSIS_DAYS = 10
EXCLUDED_PLAYERS_DAYS = 30
EXCLUDED_PLAYERS_REFRESH_DAYS = 1
TOP_PLAYERS_LIMIT = 130

FANTASY_SCORE_WEIGHTS: dict[str, float] = {
    'pts': 1,
    'fg3': 1,
    'fga': -1,
    'fg': 2,
    'fta': -1,
    'ft': 1,
    'trb': 1,
    'ast': 2,
    'stl': 4,
    'blk': 4,
    'tov': -2
}