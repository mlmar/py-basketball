from datetime import date, timedelta
from lib.db.database_table import DatabaseTable
from lib.db.client import get_client
from lib.basketball.player import Player
from lib.basketball.basketball_reference import get_data
from lib.config import SUPABASE_SAVED_DATES_TABLE, SUPABASE_PLAYER_DATA_TABLE
from util.date_util import range_of_dates

saved_dates_table = DatabaseTable[Player](SUPABASE_SAVED_DATES_TABLE)
player_data_table = DatabaseTable[Player](SUPABASE_PLAYER_DATA_TABLE)

def refresh_stats(days: int):
    """
    Retrieves stats for the last N days.
    If necessary, scrape data from basketball reference and inserts to Supabase db.
    """
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
            player_data_table.insert(players) # Save new data
            print()

def get_all(days: int):
    """Fetches all player stats from the last N days"""
    refresh_stats(days)
    end_date = date.today() - timedelta(1)
    start_date = end_date - timedelta(days - 1) 
    response = player_data_table.get_table().select('*').gte('date', str(start_date)).lte('date', str(end_date)).execute()
    return response.data

def get_averages(days: int):
    """Fetches all player averages from the last N days"""
    refresh_stats(days)
    end_date = date.today() - timedelta(1)
    start_date = end_date - timedelta(days - 1) 
    response = get_client().rpc('get_averages', {
        'start_date': str(start_date),
        'end_date': str(end_date)
    }).execute()
    return response.data

def get_totals(days: int):
    """Fetches all player totals from the last N days"""
    refresh_stats(days)
    end_date = date.today() - timedelta(1)
    start_date = end_date - timedelta(days - 1) 
    response = get_client().rpc('get_totals', {
        'start_date': str(start_date),
        'end_date': str(end_date)
    }).execute()
    return response.data