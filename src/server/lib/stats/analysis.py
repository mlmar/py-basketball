from datetime import date
from functools import partial
from typing import List

from fastapi import HTTPException, status
from pydantic import BaseModel
from lib.basketball.player import Player, ProjectedPlayer, TrendingPlayer
from lib.db.database_table import DatabaseTable
from lib.ai import gemini
from lib.stats import stats 
import config
import json
import asyncio
import traceback

from util.date_util import get_today_pst

projected_analysis_status_table = DatabaseTable(config.SUPABASE_PROJECTED_ANALYSIS_STATUS_TABLE)
projected_analysis_data_table = DatabaseTable(config.SUPABASE_PROJECTED_ANALYSIS_DATA_TABLE)
trending_analysis_status_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_STATUS_TABLE)
trending_analysis_data_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_DATA_TABLE)

class ProjectedAnalysisResult(BaseModel):
    result: List[ProjectedPlayer] = []
    status: str = 'PROCESSING'
    is_all_records: bool = True

class TrendingAnalysisResult(BaseModel):
    result: List[TrendingPlayer] = []
    status: str = 'PROCESSING'
    is_all_records: bool = True

# PROJECTED ANALYSIS
def get_projected_analysis(date_str: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> ProjectedAnalysisResult:
    """Gets most recent analysis and runs today's if it does not exist"""
    target_date = __validate_date_str(date_str)
    result = __get_result(projected_analysis_status_table, projected_analysis_data_table, target_date if date_str else None, limit)
    status = __get_status(projected_analysis_status_table, target_date)
    if status not in ['PROCESSING','COMPLETE']:
        # If today has not been processed, then start processing the data
        projected_analysis_status_table.insert({
            'date': target_date,
            'status': 'PROCESSING'
        })
        func = partial(run_projected_analysis, target_date)
        asyncio.get_running_loop().run_in_executor(None, func)
        
    return {
        'result': result,
        'status': status if status else 'PROCESSING',
        'is_all_records': limit == -1 or limit >= config.ANALYSIS_PLAYER_LIMIT
    }
    
def run_projected_analysis(target_date: str) -> list[Player]:
    """Runs projected analysis and updates today's status"""
    days = config.ANALYSIS_DAYS
    result = []

    try:
        data = stats.get_all(days, True)
        result = gemini.get_projected_analysis(data, days)
        for projectedPlayer in result:
            projected_analysis_data_table.insert({
                'date': target_date,
                'player': projectedPlayer
            }) # Save analysis data

        projected_analysis_status_table.insert({
            'date': target_date,
            'status': 'COMPLETE'
        })
    except:
        # Update status if failed
        error_str = traceback.format_exc()
        projected_analysis_status_table.insert({
            'date': target_date,
            'status': 'FAILED',
            'log': error_str
        })
        print(error_str)

    return result

# TRENDING ANALYSIS
def get_trending_analysis(date_str: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> TrendingAnalysisResult:
    target_date = __validate_date_str(date_str)
    result = __get_result(trending_analysis_status_table, trending_analysis_data_table, target_date if date_str else None, limit)
    status = __get_status(trending_analysis_status_table, target_date)
    if status not in ['PROCESSING','COMPLETE']:
        # If today has not been processed, then start processing the data
        trending_analysis_status_table.insert({
            'date': target_date,
            'status': 'PROCESSING'
        })
        func = partial(run_trending_analysis, target_date)
        asyncio.get_running_loop().run_in_executor(None, func)
    
    return {
        'result': result,
        'status': status if status else 'PROCESSING',
        'is_all_records': limit >= config.ANALYSIS_PLAYER_LIMIT
    }
    
def run_trending_analysis(target_date: str) -> list[Player]:
    """Runs trending analysis and updates today's status"""
    days = config.ANALYSIS_DAYS
    result = []

    try:
        data = stats.get_all(days, True)
        result = gemini.get_trending_analysis(data, days)
        for projectedPlayer in result:
            trending_analysis_data_table.insert({
                'date': target_date,
                'player': projectedPlayer
            }) # Save analysis data

        trending_analysis_status_table.insert({
            'date': target_date,
            'status': 'COMPLETE'
        })
    except:
        # Update status if failed
        error_str = traceback.format_exc()
        trending_analysis_status_table.insert({
            'date': target_date,
            'status': 'FAILED',
            'log': error_str
        })
        print(error_str)

    return result
    
# HELEPRS
def __get_status(status_table: DatabaseTable, current_date: str):
    status_response = status_table.get_table().select('status').eq('date', current_date).execute()
    if status_response.data is None or len(status_response.data) == 0:
        return None
    return status_response.data[0]['status']
    
def __get_result(status_table: DatabaseTable, data_table: DatabaseTable, date_str: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT):
    # If day has been processsed or completed then pull from the most recent data set
    date_response = None
    if date_str: # pull response for specific date
        date_response = status_table.get_table().select('date').eq('date', date_str).order('date', desc=True).limit(1).execute()
    else: # pull response for latest date
        date_response = status_table.get_table().select('date').eq('status', 'COMPLETE').order('date', desc=True).limit(1).execute()

    if date_response and date_response.data is not None and len(date_response.data) > 0:
        target_date = date_response.data[0]['date']
        results = data_table.get_table().select('*').eq('date', target_date).order('player->>rank').limit(limit if limit > -1 else config.ANALYSIS_PLAYER_LIMIT).execute()
        return [row['player'] for row in results.data]
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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invaid date format. Use format YYYY-MM-DD')