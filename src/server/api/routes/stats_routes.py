"""Routes for retrieving player statistics"""
from fastapi import APIRouter, Depends
from api.auth import get_current_user
from lib.stats import stats

router = APIRouter()

#  current_user: dict = Depends(get_current_user)
@router.get('/averages/{days}')
def get_averages(days: int,):
    days = min(days, 10)
    return stats.get_averages(days)

#  current_user: dict = Depends(get_current_user)
@router.get('/totals/{days}')
def get_totals(days: int,):
    days = min(days, 10)
    return stats.get_totals(days)

#  current_user: dict = Depends(get_current_user)
@router.get('/analysis')
def get_analysis():
    return stats.get_analysis()

#  current_user: dict = Depends(get_current_user)
@router.get('/trending-analysis')
def get_trending_analysis():
    return stats.get_trending_analysis()