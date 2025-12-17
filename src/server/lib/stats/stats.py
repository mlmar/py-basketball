from datetime import date, timedelta
from lib.db.database_table import DatabaseTable
from lib.db.client import get_client
from lib.basketball.player import Player
from lib.basketball.nba import get_data
from lib.stats.excluded_players import get_excluded_players
from service import daily_service
from util.date_util import get_today_pst, range_of_dates
import config

saved_dates_table = DatabaseTable[Player](config.SUPABASE_SAVED_DATES_TABLE)
player_data_table = DatabaseTable[Player](config.SUPABASE_PLAYER_DATA_TABLE)

def __get_start_end_dates(days: int) -> tuple[date, date]:
    end_date = get_today_pst() - timedelta(1)
    start_date = end_date - timedelta(days - 1)
    return (start_date, end_date)

def refresh_stats(days: int):
    """
    Retrieves stats for the last N days.
    If necessary, scrape data from basketball reference and inserts to Supabase db.
    """
    if config.DAILY_SERVER_URL: # Workaround for github actions since NBA API is blocked
        print('Daily server url exists, ignoring procedure and calling proxy instead')
        daily_service.get(f'/totals/{config.ANALYSIS_DAYS}')
        return

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

def get_all(days: int, exclude: bool = False) -> list:
    """Fetches all player stats from the last N days"""
    print(f'Fetching all player stats from the last {days} days')
    if days <= 0:
        return []
    
    refresh_stats(days)
    start_date, end_date = __get_start_end_dates(days)
    response = player_data_table.get_table().select('*').gte('date', str(start_date)).lte('date', str(end_date)).order('player').execute()
    print(f'Successfully queried database for player stats from {str(start_date)} to {str(end_date)}')
    
    if exclude:
        return __filter_excluded_players(response.data)
    return response.data

def get_averages(days: int, exclude: bool = False) -> list:
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

    if exclude:
        return __filter_excluded_players(response.data)
    return response.data

def get_totals(days: int, exclude: bool = False):
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

    if exclude:
        return __filter_excluded_players(response.data)
    return response.data

def get_top_players(days: int, min_mp: int, min_fantasy_score: int):
    """Fetches top players from the last N days"""
    print(f'Fetching top players from the last {days} days')
    if days <= 0:
        return []
    
    refresh_stats(days)
    
    start_date, end_date = __get_start_end_dates(days)
    response = get_client().rpc('get_top_players', {
        'start_date': str(start_date),
        'end_date': str(end_date),
        'min_mp': min_mp,
        'min_fantasy_score': min_fantasy_score
    }).execute()
    print(f'Successfully queried database for player totals from {str(start_date)} to {str(end_date)}')

    return response.data

def __filter_excluded_players(data: Player) -> list[Player]:
    """Filter excluded player names from data set"""
    excluded_players = get_excluded_players()
    
    is_excluded_results: dict[str, bool] = {} # cache results for whether a player name is excluded or not
    def is_excluded(name: str):
        # checks if player starts with the excluded player name (workaround for players like Jimmy Butler III)
        if name not in is_excluded_results: # cache results once
            is_excluded_results[name] = len(list(filter(name.startswith, excluded_players))) > 0
        return is_excluded_results[name]
    
    return [row for row in data if not is_excluded(row['player'])] 