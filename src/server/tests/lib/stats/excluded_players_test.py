import unittest

from lib.stats.excluded_players import get_excluded_players

class TestExcludedPlayers(unittest.TestCase):
    def test_get_excluded_players(self):
        """get_excluded_players(dates) returns a list of player names"""
        player_names = get_excluded_players()
        self.assertTrue(len(player_names) > 0)

if __name__ == '__main__':
    unittest.main()