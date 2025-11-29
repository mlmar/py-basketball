import unittest
import csv
from datetime import date
from lib.basketball.player import Player
from lib.basketball.nba import get_data
from util.date_util import range_of_dates

class TestNBA(unittest.TestCase):
    def test_get_data(self):
        """get_data(dates) yields a list of players"""
        dates = list(range_of_dates(date(2025,11,10), date(2025,11,11)))
        for (current_date, players) in get_data(dates):
            self.assertIsNotNone(current_date)
            self.assertTrue(len(players) > 0)

    def test_data_to_csv(self):
        assert True # skip this test
        
        dates = list(range_of_dates(date(2025,10,21), date.today()))
        with open('data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow({
                'id': '',
                'player': '',
                'team_id': '',
                'opp_id': '',
                'mp': '',
                'fg': '',
                'fga': '',
                'fg_pct': '',
                'fg3': '',
                'fg3a': '',
                'fg3_pct': '',
                'ft': '',
                'fta': '',
                'ft_pct': '',
                'orb': '',
                'drb': '',
                'trb': '',
                'ast': '', 
                'stl': '', 
                'blk': '', 
                'tov': '', 
                'pts': '', 
                'plus_minus': '',
                'date': '', 
            })
            for (current_date, players) in get_data(dates):
                for player in players:
                    writer.writerow([
                        player['id'],
                        player['player'],
                        player['team_id'],
                        player['opp_id'],
                        player['mp'],
                        player['fg'],
                        player['fga'],
                        player['fg_pct'],
                        player['fg3'],
                        player['fg3a'],
                        player['fg3_pct'],
                        player['ft'],
                        player['fta'],
                        player['ft_pct'],
                        player['orb'],
                        player['drb'],
                        player['trb'],
                        player['ast'], 
                        player['stl'], 
                        player['blk'], 
                        player['tov'], 
                        player['pts'], 
                        player['plus_minus'],
                        player['date']
                    ])

if __name__ == '__main__':
    unittest.main()