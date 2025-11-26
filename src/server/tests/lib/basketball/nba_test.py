import unittest
from datetime import date

from lib.basketball.nba import get_data
from util.date_util import range_of_dates

class TestNBA(unittest.TestCase):
    def test_get_data(self):
        """get_data(dates) yields a list of players"""
        dates = list(range_of_dates(date(2025,11,10), date(2025,11,11)))
        for (current_date, players) in get_data(dates):
            self.assertIsNotNone(current_date)
            self.assertTrue(len(players) > 0)


if __name__ == '__main__':
    unittest.main()