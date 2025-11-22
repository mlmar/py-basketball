import unittest
from service.nba_cdn_service import get_nba_schedule, __game_date_from_str
from datetime import date, datetime

class TestNBACDNService(unittest.TestCase):
    def test_get_nba_schedule_all(self):
        """get_nba_schedule() returns list of NBA games for the season"""
        schedule = get_nba_schedule()
        self.assertGreater(len(schedule), 0)

    def test_get_nba_schedule_future(self):
        """get_nba_schedule() returns list of NBA games for the rest of the season"""
        today = date.today()
        schedule = get_nba_schedule(today)
        for game_day in schedule:
            self.assertGreaterEqual(date_from_str(game_day['date']), today)


def date_from_str(game_date_str: str) -> date:
    format_code = '%Y-%m-%d'
    datetime_result = datetime.strptime(game_date_str, format_code)
    return datetime_result.date()