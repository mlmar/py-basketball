from datetime import date, timedelta
from lib.db.database_table import DatabaseTable
from lib.db.client import get_client
from lib.basketball.player import Player
from lib.basketball.nba import get_data
from lib.ai import gemini
from util.date_util import range_of_dates
import config
import json

saved_dates_table = DatabaseTable[Player](config.SUPABASE_SAVED_DATES_TABLE)
player_data_table = DatabaseTable[Player](config.SUPABASE_PLAYER_DATA_TABLE)
analysis_status_table = DatabaseTable(config.SUPABASE_ANALYSIS_STATUS_TABLE)
analysis_data_table = DatabaseTable(config.SUPABASE_ANALYSIS_DATA_TABLE)
trending_analysis_status_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_STATUS_TABLE)
trending_analysis_data_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_DATA_TABLE)

def __get_start_end_dates(days: int) -> tuple[date, date]:
    end_date = date.today() - timedelta(1)
    start_date = end_date - timedelta(days - 1)
    return (start_date, end_date)

def refresh_stats(days: int):
    """
    Retrieves stats for the last N days.
    If necessary, scrape data from basketball reference and inserts to Supabase db.
    """
    start_date, end_date = __get_start_end_dates(days)

    # Filter out existing dates
    all_dates: list[date] = list(range_of_dates(start_date, end_date))
    response = saved_dates_table.get_table().select('date').in_('date', [str(d) for d in all_dates]).execute()
    existing_dates: list[date] = [item['date'] for item in response.data]
    new_dates: list[date] = [new_date for new_date in all_dates if str(new_date) not in existing_dates]

    print('Existing Dates: ', existing_dates)
    print('New Dates: ', [str(d) for d in new_dates])

    # Insert data for newly saved dates
    if len(new_dates) > 0:
        for (current_date, players) in get_data(new_dates):
            if players is not None and len(players) > 0:
                player_data_table.insert(players) # Save new data
                saved_dates_table.insert({ 'date': str(current_date) }) # Save the date
            print()

def get_all(days: int):
    """Fetches all player stats from the last N days"""
    print(f'Fetching all player stats from the last {days} days')
    if days <= 0:
        return []
    
    refresh_stats(days)
    start_date, end_date = __get_start_end_dates(days)
    response = player_data_table.get_table().select('*').gte('date', str(start_date)).lte('date', str(end_date)).order('player').execute()
    print(f'Successfully queried database for player stats from {str(start_date)} to {str(end_date)}')
    return response.data

def get_averages(days: int):
    """Fetches all player averages from the last N days"""
    print(f'Fetching all player averages from the last {days} days')
    if days <= 0:
        return []
    
    refresh_stats(days)

    start_date, end_date = __get_start_end_dates(days)
    response = get_client().rpc('get_averages', {
        'start_date': str(start_date),
        'end_date': str(end_date)
    }).execute()
    print(f'Successfully queried database for player averages from {str(start_date)} to {str(end_date)}')
    return response.data

def get_totals(days: int):
    """Fetches all player totals from the last N days"""
    print(f'Fetching all player totals from the last {days} days')
    if days <= 0:
        return []
    
    refresh_stats(days)
    
    start_date, end_date = __get_start_end_dates(days)
    response = get_client().rpc('get_totals', {
        'start_date': str(start_date),
        'end_date': str(end_date)
    }).execute()
    print(f'Successfully queried database for player totals from {str(start_date)} to {str(end_date)}')
    return response.data

most_recent_data = None # Store most recent data locally

def get_analysis():
    """Gets most recent analysis or runs today's if it does not exist"""
    global most_recent_data
    if most_recent_data is not None:
        return most_recent_data

    today = str(date.today())
    days = 10

    status_response = analysis_status_table.get_table().select('status').eq('date', today).execute()
    if status_response.data is None or len(status_response.data) == 0:
        data = get_all(days)

        # If today has not been processed, then start processing the data
        analysis_status_table.insert({
            'date': today,
            'status': 'PROCESSING'
        })

        try:
            result = gemini.get_analysis(data, days)
            for projectedPlayer in result:
                analysis_data_table.insert({
                    'date': today,
                    'player': json.dumps(projectedPlayer)
                }) # Save anaylsis data

            analysis_status_table.insert({
                'date': today,
                'status': 'COMPLETE'
            })
        except:
            # Update status if failed
            analysis_status_table.insert({
                'date': today,
                'status': 'FAILED'
            })
        most_recent_data = result;
        return result
    elif status_response.data[0]['status'] == 'PROCESSING' or status_response.data[0]['status']  == 'COMPLETE':
        # If day has been processsed or completed then pull from the most recent data set
        date_response = analysis_status_table.get_table().select('date').not_.is_('status', 'FAILED').order('date', desc=True).limit(1).execute()
        if date_response.data is not None or len(date_response.data) > 0:
            recent_date = date_response.data[0]['date']
            results = analysis_data_table.get_table().select('*').eq('date', recent_date).execute()
            most_recent_data = [json.loads(row['player']) for row in results.data]
            return most_recent_data
        else:
            return []
    else:
        return []

def get_trending_analysis():
    """Gets most recent trending analysis or runs today's if it does not exist"""
    global most_recent_data
    if most_recent_data is not None:
        return most_recent_data

    today = str(date.today())
    days = 10

    status_response = trending_analysis_status_table.get_table().select('status').eq('date', today).execute()
    if status_response.data is None or len(status_response.data) == 0:
        data = get_all(days)

        # If today has not been processed, then start processing the data
        trending_analysis_status_table.insert({
            'date': str(date.today()),
            'status': 'PROCESSING'
        })

        result = gemini.get_trending_analysis(data, days)
        for projectedPlayer in result:
            trending_analysis_data_table.insert({
                'date': today,
                'player': json.dumps(projectedPlayer)
            }) # Save anaylsis data

        trending_analysis_status_table.insert({
            'date': str(date.today()),
            'status': 'COMPLETE'
        })
        
        most_recent_data = result;
        return result
    elif status_response.data[0]['status'] == 'PROCESSING' or status_response.data[0]['status']  == 'COMPLETE':
        # If day has been processsed or completed then pull from the most recent data set
        date_response = analysis_status_table.get_table().select('date').order('date', desc=True).limit(1).execute()
        if date_response.data is not None or len(date_response.data) > 0:
            recent_date = date_response.data[0]['date']
            results = trending_analysis_data_table.get_table().select('*').eq('date', recent_date).execute()
            most_recent_data = [json.loads(row['player']) for row in results.data]
            return most_recent_data
        else:
            return []
    else:
        return []