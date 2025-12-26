"""Exposing env variables as config props"""

import os
from dotenv import load_dotenv

load_dotenv()
DEV: str = os.environ.get('DEV')
CLIENT_URL: str = os.environ.get('VITE_CLIENT_URL')
SERVER_URL: str = os.environ.get('VITE_SERVER_URL')
DAILY_SERVER_URL: str = os.environ.get('VITE_DAILY_SERVER_URL')
SUPABASE_URL: str = os.environ.get('SUPABASE_URL')
SUPABASE_KEY: str = os.environ.get('SUPABASE_KEY')
SUPABASE_JWT_SECRET: str = os.environ.get('SUPABASE_JWT_SECRET')

SUPABASE_SCHEMA = 'waiverwarrior'
SUPABASE_SAVED_DATES_TABLE: str = 'saved_dates'
SUPABASE_PLAYER_DATA_TABLE: str = 'player_data'
SUPABASE_PROJECTED_ANALYSIS_STATUS_TABLE: str = 'projected_analysis_status'
SUPABASE_PROJECTED_ANALYSIS_DATA_TABLE: str = 'projected_analysis_data'
SUPABASE_TRENDING_ANALYSIS_STATUS_TABLE: str = 'trending_analysis_status'
SUPABASE_TRENDING_ANALYSIS_DATA_TABLE: str = 'trending_analysis_data'
SUPABASE_EXCLUDED_PLAYERS_TABLE: str = 'excluded_players'
SUPABASE_TOKENS_TABLE: str = 'tokens'

ANALYSIS_PLAYER_LIMIT: int = 20
ANALYSIS_DAYS: int = 10
EXCLUDED_PLAYERS_DAYS: int = 30
EXCLUDED_PLAYERS_REFRESH_DAYS: int = 1
TOP_PLAYERS_LIMIT: int = 130
TOP_PLAYERS_MIN_MP: int = 22
TOP_PLAYERS_MIN_FANTASY_SCORE: int = 23

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

# Yahoo OAuth credentials (set via environment or .env)
YAHOO_CLIENT_ID: str = os.environ.get('YAHOO_CLIENT_ID')
YAHOO_CLIENT_SECRET: str = os.environ.get('YAHOO_CLIENT_SECRET')
YAHOO_REDIRECT_URL: str = os.environ.get('YAHOO_REDIRECT_URL')