"""Exposing env variables as config props"""

import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL: str = os.environ.get('SUPABASE_URL')
SUPABASE_KEY: str = os.environ.get('SUPABASE_KEY')
SUPABASE_SAVED_DATES_TABLE: str = os.environ.get('SUPABASE_SAVED_DATES_TABLE')
SUPABASE_PLAYER_DATA_TABLE: str = os.environ.get('SUPABASE_PLAYER_DATA_TABLE')