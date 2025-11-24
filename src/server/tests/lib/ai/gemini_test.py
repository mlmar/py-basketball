import unittest
from lib.stats import stats
from lib.ai import gemini

class TestGemini(unittest.TestCase):
    def test_get_analysis(self):
        """get_analysis() returns a response with 10 players"""
        days = 10
        data = stats.get_all(days)
        num_players = 5
        response = gemini.get_analysis(data, days, num_players)
        self.assertEqual(len(response), num_players)

if __name__ == '__main__':
    unittest.main()