"""Exposing env variables as config props"""

import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL: str = os.environ.get('SUPABASE_URL')
SUPABASE_KEY: str = os.environ.get('SUPABASE_KEY')
SUPABASE_JWT_SECRET: str = os.environ.get('SUPABASE_JWT_SECRET')
SUPABASE_SAVED_DATES_TABLE: str = 'saved_dates'
SUPABASE_PLAYER_DATA_TABLE: str = 'player_data'
SUPABASE_PROJECTED_ANALYSIS_STATUS_TABLE: str = 'projected_analysis_status'
SUPABASE_PROJECTED_ANALYSIS_DATA_TABLE: str = 'projected_analysis_data'
SUPABASE_TRENDING_ANALYSIS_STATUS_TABLE: str = 'trending_analysis_status'
SUPABASE_TRENDING_ANALYSIS_DATA_TABLE: str = 'trending_analysis_data'