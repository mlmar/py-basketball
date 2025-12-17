from datetime import date
from enum import Enum
from functools import partial
from typing import List

from fastapi import HTTPException, status
from pydantic import BaseModel
from lib.basketball.player import ProjectedPlayer, TrendingPlayer
from lib.db.client import get_client
from lib.db.database_table import DatabaseTable
from lib.ai import gemini
from lib.stats import stats 
import config
import asyncio
import traceback

from util.date_util import get_today_pst

projected_analysis_status_table = DatabaseTable(config.SUPABASE_PROJECTED_ANALYSIS_STATUS_TABLE)
projected_analysis_data_table = DatabaseTable(config.SUPABASE_PROJECTED_ANALYSIS_DATA_TABLE)
projected_analysis_data_method = 'get_projected_analysis_data'
trending_analysis_status_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_STATUS_TABLE)
trending_analysis_data_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_DATA_TABLE)
trending_analysis_data_method = 'get_trending_analysis_data'

class Status(Enum):
    COMPLETE: str = 'COMPLETE'
    PROCESSING: str = 'PROCESSING'
    FAILED: str = 'FAILED'

class ProjectedAnalysisResult(BaseModel):
    result: List[ProjectedPlayer] = []
    status: str = Status.PROCESSING.value
    is_all_records: bool = True

class TrendingAnalysisResult(BaseModel):
    result: List[TrendingPlayer] = []
    status: str = Status.PROCESSING.value
    is_all_records: bool = True

# PROJECTED ANALYSIS
def get_projected_analysis(date_str: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> ProjectedAnalysisResult:
    """Gets most recent projected analysis"""
    target_date = __validate_date_str(date_str) if date_str else None


    try:
        result = __get_result(projected_analysis_status_table, projected_analysis_data_method, target_date, limit)
        status = __get_status(projected_analysis_status_table, target_date)
        # is_processing = __is_status_processing(projected_analysis_status_table) # Prevent run if anything is currently processing
        # if not is_processing and status not in [Status.PROCESSING.value, Status.COMPLETE.value]:
        #     # If today has not been processed, then start processing the data
        #     func = partial(run_projected_analysis, target_date)
        #     asyncio.get_running_loop().run_in_executor(None, func)
            
        return {
            'result': result,
            'status': status if status else Status.PROCESSING.value,
            'is_all_records': limit == -1 or limit >= config.ANALYSIS_PLAYER_LIMIT
        }
    except:
        print(f'An error occurred while fetching projected data for ${target_date}')
        traceback.print_exc()
        return {
            'result': [],
            'status': Status.FAILED.value,
            'is_all_records': True
        }
    
def run_projected_analysis(target_date: str) -> list[ProjectedPlayer]:
    """Runs projected analysis and updates today's status"""
    days = config.ANALYSIS_DAYS
    result = []

    try:
        projected_analysis_status_table.insert({
            'date': target_date,
            'status': Status.PROCESSING.value
        })

        data = stats.get_all(days, True)
        result = gemini.get_projected_analysis(data, days)
        for projected_player in result:
            projected_player['date'] = target_date
            projected_analysis_data_table.insert({
                'date': target_date,
                'player': projected_player['player'],
                'num_games': projected_player['num_games'],
                'opponents': projected_player['opponents'],
                'game_dates': projected_player['game_dates'],
                'analysis': projected_player['analysis'],
                'tags': projected_player['tags'],
                'rank': projected_player['rank'],
            }) # Save analysis data

        projected_analysis_status_table.insert({
            'date': target_date,
            'status': Status.COMPLETE.value
        })
    except:
        # Update status if failed
        error_str = traceback.format_exc()
        projected_analysis_status_table.insert({
            'date': target_date,
            'status': Status.FAILED.value,
            'log': error_str
        })
        print(error_str)

    return result

# TRENDING ANALYSIS
def get_trending_analysis(date_str: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> TrendingAnalysisResult:
    """Gets most recent trending analysis"""
    target_date = __validate_date_str(date_str) if date_str else None

    try:
        result = __get_result(trending_analysis_status_table, trending_analysis_data_method, target_date, limit)
        status = __get_status(trending_analysis_status_table, target_date)
        # is_processing = __is_status_processing(trending_analysis_status_table)  # Prevent run if anything is currently processing
        # if not is_processing and status not in [Status.PROCESSING.value, Status.COMPLETE.value]:
        #     func = partial(run_trending_analysis, target_date)
        #     asyncio.get_running_loop().run_in_executor(None, func)
        
        return {
            'result': result,
            'status': status if status else Status.PROCESSING.value,
            'is_all_records': limit >= config.ANALYSIS_PLAYER_LIMIT
        }
    except:
        print(f'An error occurred while fetching trending data for ${target_date}')
        traceback.print_exc()
        return {
            'result': [],
            'status': Status.FAILED.value,
            'is_all_records': True
        }
    
def run_trending_analysis(target_date: str) -> list[TrendingPlayer]:
    """Runs trending analysis and updates today's status"""
    days = config.ANALYSIS_DAYS
    result = []

    try:
        trending_analysis_status_table.insert({
            'date': target_date,
            'status': Status.PROCESSING.value
        })

        data = stats.get_all(days, True)
        result = gemini.get_trending_analysis(data, days)
        for trending_player in result:
            trending_player['date'] = target_date
            trending_analysis_data_table.insert({
                'date': target_date,
                'player': trending_player['player'],
                'num_games': trending_player['num_games'],
                'opponents': trending_player['opponents'],
                'game_dates': trending_player['game_dates'],
                'analysis': trending_player['analysis'],
                'tags': trending_player['tags'],
                'rank': trending_player['rank']
            }) # Save analysis data

        trending_analysis_status_table.insert({
            'date': target_date,
            'status': Status.COMPLETE.value
        })
    except:
        # Update status if failed
        error_str = traceback.format_exc()
        trending_analysis_status_table.insert({
            'date': target_date,
            'status': Status.FAILED.value,
            'log': error_str
        })
        print(error_str)

    return result
    
# HELEPRS
def __get_status(status_table: DatabaseTable, current_date: str) -> str | None:
    """Gets status for specific date from status table"""
    
    status_response = None
    if current_date: # get status for current date
        status_response = status_table.get_table().select('status').eq('date', current_date).execute()
    else: # get status for latest date
        status_response = status_table.get_table().select('status').order('date', desc=True).limit(1).execute()

    if status_response.data is None or len(status_response.data) == 0:
        return None
    return status_response.data[0]['status']

def __is_status_processing(status_table: DatabaseTable) -> bool:
    """Checks if any dates are currently processing"""
    status_response = status_table.get_table().select('status').eq('status', Status.PROCESSING.value).execute()
    if status_response.data is None or len(status_response.data) == 0:
        return False
    return True
    
def __get_result(status_table: DatabaseTable, method: str, date_str: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT):
    # If day has been processsed or completed then pull from the most recent data set
    date_response = None
    if date_str: # pull response for specific date
        date_response = status_table.get_table().select('date').eq('date', date_str).order('date', desc=True).limit(1).execute()
    else: # pull response for latest date
        date_response = status_table.get_table().select('date').eq('status', 'COMPLETE').order('date', desc=True).limit(1).execute()

    if date_response and date_response.data is not None and len(date_response.data) > 0:
        target_date = date_response.data[0]['date']
        results = get_client().rpc(method, {
            'target_date': str(target_date),
            'row_limit': limit if limit > -1 else config.ANALYSIS_PLAYER_LIMIT
        }).execute()
        return results.data
    else:
        return []

    
def __validate_date_str(date_str: str) -> str:
    """Validates date string by attempting to convert it to a date and back"""
    try:
        if date_str:
            y, m, d = date_str.split('-')
            return str(date(int(y), int(m), int(d)))
        else:
            return str(get_today_pst())
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST.value, detail='Invaid date format. Use format YYYY-MM-DD')