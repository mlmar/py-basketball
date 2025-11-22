import unittest
from datetime import date

from lib.basketball.basketball_reference import get_url, get_data
from util.date_util import range_of_dates


class TestBasketballReference(unittest.TestCase):
    def test_get_url_returns_correct_query(self):
        """get_url(date) includes year, month, and day for a valid date"""
        test_date = date(2025, 11, 3)
        url = get_url(test_date)
        self.assertIn(f'year={test_date.year}', url)
        self.assertIn(f'month={test_date.month}', url)
        self.assertIn(f'day={test_date.day}', url)

    def test_get_url_raises_when_date_none(self):
        """get_url() should raise when called with None"""
        with self.assertRaises(Exception):
            get_url(None)

    def test_get_data(self):
        dates = list(range_of_dates(date(2025,11,10), date(2025,11,11)))
        for (current_date, players) in get_data(dates):
            self.assertIsNotNone(current_date)
            self.assertTrue(len(players) > 0)


if __name__ == '__main__':
    unittest.main()