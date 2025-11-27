"""Exposing env variables as config props"""

import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL: str = os.environ.get('SUPABASE_URL')
SUPABASE_KEY: str = os.environ.get('SUPABASE_KEY')
SUPABASE_JWT_SECRET: str = os.environ.get('SUPABASE_JWT_SECRET')
SUPABASE_SAVED_DATES_TABLE: str = os.environ.get('SUPABASE_SAVED_DATES_TABLE')
SUPABASE_PLAYER_DATA_TABLE: str = os.environ.get('SUPABASE_PLAYER_DATA_TABLE')
SUPABASE_ANALYSIS_STATUS_TABLE: str = os.environ.get('SUPABASE_ANALYSIS_STATUS_TABLE')
SUPABASE_ANALYSIS_DATA_TABLE: str = os.environ.get('SUPABASE_ANALYSIS_DATA_TABLE')