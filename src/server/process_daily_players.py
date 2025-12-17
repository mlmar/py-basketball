import config
from lib.stats.analysis import run_trending_analysis
from service.daily_service import daily_service
from util.date_util import get_today_pst

def run_daily_trending_analysis():
    """Inserts status to db, runs trending analysis, and inserts result to db"""
    today_date_str = str(get_today_pst())
    daily_service.get(f'/totals/{config.ANALYSIS_DAYS}')
    run_trending_analysis(today_date_str)

if __name__ == '__main__':
    run_daily_trending_analysis()