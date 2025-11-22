import unittest
from util.date_util import range_of_dates
from datetime import date

class TestDateUtil(unittest.TestCase):
    def test_range_of_dates_same_year(self):
        """range_of_dates() returns valid range for start date and end date within the same year"""
        dates: list[date] = [date(2025,12,1), date(2025,12,2), date(2025,12,3), date(2025,12,4)]
        result = list(range_of_dates(dates[0], dates[-1]))
        self.assertListEqual(dates, result)

    def test_range_of_dates_different_year(self):
        """range_of_dates() returns valid range for start date and end date with different years"""
        dates: list[date] = [date(2025,12,30), date(2025,12,31), date(2026,1,1), date(2026,1,2)]
        result = list(range_of_dates(dates[0], dates[-1]))
        self.assertListEqual(dates, result)