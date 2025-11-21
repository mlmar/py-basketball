from datetime import date, timedelta
from lib.db.client import get_client
from lib.db.database_table import DatabaseTable
from lib.basketball.basketball_reference import get_data
from lib.config import SUPABASE_PLAYER_TABLE

get_client()

print()
days = int(input('Last N Days: '))
end_date = date.today()
start_date = end_date - timedelta(days - 1)

table = DatabaseTable(SUPABASE_PLAYER_TABLE)

for (current_date, players) in get_data(start_date, end_date):
    table.insert_players(players)