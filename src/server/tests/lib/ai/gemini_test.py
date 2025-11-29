import unittest
from lib.stats import stats
from lib.ai import gemini

class TestGemini(unittest.TestCase):
    def test_get_projected_analysis(self):
        """get_projected_analysis() returns a response with 10 players"""
        days = 10
        data = stats.get_all(days)
        num_players = 10
        response = gemini.get_projected_analysis(data, days, num_players)
        self.assertEqual(len(response), num_players)

    def test_get_projected_analysis(self):
        """get_projected_analysis() returns a response with 10 players"""
        days = 10
        data = stats.get_all(days)
        num_players = 10
        response = gemini.get_projected_analysis(data, days, num_players)
        self.assertEqual(len(response), num_players)

    def test_get_trending_analysis(self):
        """get_trending_analysis() returns a response with 20 players"""
        days = 10
        data = stats.get_all(days)
        num_players = 20
        response = gemini.get_trending_analysis(data, days, num_players)
        self.assertEqual(len(response), num_players)


if __name__ == '__main__':
    unittest.main()