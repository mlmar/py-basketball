from datetime import date, timedelta
from lib.db.database_table import DatabaseTable
from lib.basketball.player import Player
from lib.basketball.basketball_reference import get_data
from lib.config import SUPABASE_SAVED_DATES_TABLE, SUPABASE_PLAYER_TABLE
from util.date_util import range_of_dates

saved_dates_table = DatabaseTable[Player](SUPABASE_SAVED_DATES_TABLE)
player_table = DatabaseTable[Player](SUPABASE_PLAYER_TABLE)

print()
days = int(input('Last N Days (Excluding today): '))
end_date = date.today() - timedelta(1)
start_date = end_date - timedelta(days - 1)

# Filter out existing dates
all_dates: list[date] = list(range_of_dates(start_date, end_date))
response = saved_dates_table.get_table().select('date').in_('date', [str(d) for d in all_dates]).execute()
existing_dates: list[date] = [item['date'] for item in response.data]
new_dates: list[date] = [new_date for new_date in all_dates if str(new_date) not in existing_dates]

print('Existing Dates: ', existing_dates)
print('New Dates: ', [str(d) for d in new_dates])
print('------')

# Insert data for newly saved dates
if len(new_dates) > 0:
    for (current_date, players) in get_data(new_dates):
        saved_dates_table.insert({ 'date': str(current_date) }) # Save the date
        player_table.insert(players) # Save new data
        print()