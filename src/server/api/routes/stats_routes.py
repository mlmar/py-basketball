"""Routes for retrieving player statistics"""
from fastapi import APIRouter
import config
from lib.stats import stats, analysis

router = APIRouter()

@router.get('/averages/{days}')
def get_averages(days: int, exclude: bool = False):
    days = min(days, 10)
    return stats.get_averages(days, exclude)

@router.get('/totals/{days}')
def get_totals(days: int, exclude: bool = False):
    days = min(days, 10)
    return stats.get_totals(days, exclude)

@router.get('/top-players')
def get_totals(days: int = 30, min_mp: int = 0, min_fantasy_score: int = 0):
    return stats.get_top_players(days, min_mp, min_fantasy_score)

@router.get('/projected-analysis')
async def get_projected_analysis(date: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> analysis.ProjectedAnalysisResult:
    return analysis.get_projected_analysis(date, limit)

@router.get('/trending-analysis')
async def get_trending_analysis(date: str = None, limit: int = config.ANALYSIS_PLAYER_LIMIT) -> analysis.TrendingAnalysisResult:
    return analysis.get_trending_analysis(date, limit)