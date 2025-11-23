import unittest
from lib.stats import stats
from lib.ai import gemini

class TestGemini(unittest.TestCase):
    def test_get_analysis(self):
        """get_analysis() returns a response with 10 players"""
        days = 5
        averages = stats.get_averages(days)
        response = gemini.get_analysis(averages, 'averages', days)
        self.assertEqual(len(response), 10)

if __name__ == '__main__':
    unittest.main()