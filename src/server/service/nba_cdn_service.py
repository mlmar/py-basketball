from pydantic import BaseModel
from datetime import date, datetime
from service.service import Service
from util.date_util import calc_date

class Game(BaseModel):
    away_team: str
    home_team: str

class GameDay(BaseModel):
    date: date
    games: list[Game]

nba_cdn_service = Service('https://cdn.nba.com/static/json/staticData')
def get_nba_schedule(start_date: date = None, num_days: int = 7) -> list[GameDay]:
    """Returns minimal and parsed NBA game schedule after the start_date"""
    response = nba_cdn_service.get('/scheduleLeagueV2.json')
    game_days = response['leagueSchedule']['gameDates']
    end_date = calc_date(start_date, num_days)
    if start_date is not None: # Filter by start date
        return [__get_game_day_info(game_day) for game_day in game_days if __game_date_from_str(game_day['gameDate']) >= start_date and __game_date_from_str(game_day['gameDate']) <= end_date]
    else: # Filter by end date
        return [__get_game_day_info(game_day) for game_day in game_days]

def __get_game_day_info(game_day_response) -> GameDay:
    """Reduces game_day_response to only include the date and list of games"""
    return {
        'date': str(__game_date_from_str(game_day_response['gameDate'])),
        'games': [__get_game_info(game) for game in game_day_response['games']]
    }

def __get_game_info(game_response) -> Game:
    """Reduces game response to away team and home team properties"""
    return {
        'away_team': game_response['awayTeam']['teamTricode'], 
        'home_team': game_response['homeTeam']['teamTricode'] 
    }

def __game_date_from_str(game_date_str: str) -> date:
    format_code = '%m/%d/%Y %H:%M:%S'
    datetime_result = datetime.strptime(game_date_str, format_code)
    return datetime_result.date()