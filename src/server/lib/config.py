# Loads environent variables

import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL: str = os.environ.get('SUPABASE_URL')
SUPABASE_KEY: str = os.environ.get('SUPABASE_KEY')
SUPABASE_PLAYER_TABLE: str = os.environ.get('SUPABASE_PLAYER_TABLE')