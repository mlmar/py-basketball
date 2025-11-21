from lib.config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client, Client

__client: Client = None

def get_client() -> Client:
    """Loads and returns connection to Supabase instance"""
    global __client
    if __client == None:
        print('Connecting to Supabase')
        __client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print('Connected to Supabase')

    return __client