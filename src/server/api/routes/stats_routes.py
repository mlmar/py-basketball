"""Routes for retrieving player statistics"""
from fastapi import APIRouter, Depends
from api.auth import get_current_user
from lib.stats import stats
from lib.ai import gemini

# from lib.stats.stats import get_all, get_averages, get_totals
# from lib.ai.gemini import get_analysis

# days = int(input('Last N Days (Excluding today, max of 10): '))
# days = min(days, 10)

# # get_all(days)
# averages = get_averages(days)
# print('------')

# get_analysis(averages, 'averages', days)

router = APIRouter()

@router.get('/averages/{days}')
def get_averages(days: int, current_user: dict = Depends(get_current_user)):
    days = min(days, 10)
    return stats.get_averages(days)

@router.get('/totals/{days}')
def get_totals(days: int, current_user: dict = Depends(get_current_user)):
    days = min(days, 10)
    return stats.get_totals(days)

@router.get('/analysis')
def get_analysis(days: int, current_user: dict = Depends(get_current_user)):
    data = stats.get_all(days)
    days = min(days, 10)
    return gemini.get_analysis(data, days)