import config
from lib.stats.analysis import run_trending_analysis
from service.service import Service
from util.date_util import get_today_pst

def run_daily_trending_analysis():
    """Inserts status to db, runs trending analysis, and inserts result to db"""
    today_date_str = str(get_today_pst())
    run_trending_analysis(today_date_str)

if __name__ == '__main__':
    run_daily_trending_analysis()