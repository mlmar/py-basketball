from datetime import date
from lib.db.database_table import DatabaseTable
from lib.ai import gemini
from lib.stats import stats 
import config
import json
import asyncio
import traceback

projected_analysis_status_table = DatabaseTable(config.SUPABASE_PROJECTED_ANALYSIS_STATUS_TABLE)
projected_analysis_data_table = DatabaseTable(config.SUPABASE_PROJECTED_ANALYSIS_DATA_TABLE)
trending_analysis_status_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_STATUS_TABLE)
trending_analysis_data_table = DatabaseTable(config.SUPABASE_TRENDING_ANALYSIS_DATA_TABLE)

# PROJECTED ANALYSIS
def get_projected_analysis():
    """Gets most recent analysis and runs today's if it does not exist"""
    result = __get_latest_result(projected_analysis_status_table, projected_analysis_data_table)
    today = str(date.today())
    status = __get_status(projected_analysis_status_table, today)
    if status is None:
        # If today has not been processed, then start processing the data
        projected_analysis_status_table.insert({
            'date': today,
            'status': 'PROCESSING'
        })
        asyncio.get_running_loop().run_in_executor(None, run_projected_analysis)
        
    return result
    
def run_projected_analysis():
    """Runs projected analysis and updates today's status"""
    today = str(date.today())
    days = 10
    data = stats.get_all(days)

    result = []

    try:
        result = gemini.get_projected_analysis(data, days)
        for projectedPlayer in result:
            projected_analysis_data_table.insert({
                'date': today,
                'player': json.dumps(projectedPlayer)
            }) # Save anaylsis data

        projected_analysis_status_table.insert({
            'date': today,
            'status': 'COMPLETE'
        })
    except:
        # Update status if failed
        error_str = traceback.format_exc()
        projected_analysis_status_table.insert({
            'date': today,
            'status': 'FAILED',
            'log': error_str
        })
        print(error_str)

    return result

# TRENDING ANALYSIS
def get_trending_analysis():
    result = __get_latest_result(trending_analysis_status_table, trending_analysis_data_table)
    today = str(date.today())
    status = __get_status(trending_analysis_status_table, today)
    if status is None:
        # If today has not been processed, then start processing the data
        trending_analysis_status_table.insert({
            'date': today,
            'status': 'PROCESSING'
        })
        asyncio.get_running_loop().run_in_executor(None, run_trending_analysis)
    
    return result
    
def run_trending_analysis():
    """Runs trending analysis and updates today's status"""
    today = str(date.today())
    days = 10
    data = stats.get_all(days)

    result = []

    try:
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
    except:
        # Update status if failed
        error_str = traceback.format_exc()
        trending_analysis_status_table.insert({
            'date': today,
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
    
def __get_latest_result(status_table: DatabaseTable, data_table: str):
    # If day has been processsed or completed then pull from the most recent data set
    date_response = status_table.get_table().select('date').eq('status', 'COMPLETE').order('date', desc=True).limit(1).execute()
    if date_response.data is not None or len(date_response.data) > 0:
        recent_date = date_response.data[0]['date']
        results = data_table.get_table().select('*').eq('date', recent_date).execute()
        return [json.loads(row['player']) for row in results.data]
    else:
        return []