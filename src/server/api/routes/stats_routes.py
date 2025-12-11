"""Routes for retrieving player statistics"""
from typing import Optional
from fastapi import APIRouter, Depends
from api.auth import get_current_user
import config
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
async def get_projected_analysis(date: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> analysis.ProjectedAnalysisResult:
    return analysis.get_projected_analysis(date, limit)

#  current_user: dict = Depends(get_current_user)
@router.get('/trending-analysis')
async def get_trending_analysis(date: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> analysis.TrendingAnalysisResult:
    return analysis.get_trending_analysis(date, limit)