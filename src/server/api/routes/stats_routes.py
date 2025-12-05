"""Routes for retrieving player statistics"""
from typing import Optional
from fastapi import APIRouter, Depends
from api.auth import get_current_user
from lib.stats import stats, analysis

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
@router.get('/projected-analysis')
async def get_projected_analysis():
    return analysis.get_projected_analysis()

#  current_user: dict = Depends(get_current_user)
@router.get('/projected-analysis/{date_str}')
async def get_projected_analysis(date_str: str):
    return analysis.get_projected_analysis(date_str)

#  current_user: dict = Depends(get_current_user)
@router.get('/trending-analysis')
async def get_trending_analysis():
    return analysis.get_trending_analysis()

#  current_user: dict = Depends(get_current_user)
@router.get('/trending-analysis/{date_str}')
async def get_trending_analysis(date_str: str):
    return analysis.get_trending_analysis(date_str)