import unittest
from lib.basketball.player import Player

class TestPlayer(unittest.TestCase):
    def test_init_empty(self):
        """Player() initializes with no attributes set"""
        player = Player()
        # Check that object exists (attributes not required until set)
        self.assertIsInstance(player, Player)

    def test_init_with_dict(self):
        """Player(dict) initializes from dictionary"""
        data = {
            'id': 'test_id',
            'player': 'LeBron James',
            'team_id': 'LAL',
            'opp_id': 'BOS',
            'mp': '32:45',
            'fg': 8.0,
            'fga': 15.0,
            'fg_pct': 0.533,
            'fg3': 2.0,
            'fg3a': 5.0,
            'fg3_pct': 0.4,
            'ft': 4.0,
            'fta': 5.0,
            'ft_pct': 0.8,
            'orb': 1.0,
            'drb': 5.0,
            'trb': 6.0,
            'ast': 7.0,
            'stl': 1.0,
            'blk': 0.0,
            'tov': 2.0,
            'pts': 22.0,
            'plus_minus': 5.0,
            'date': '2025-11-21',
        }
        player = Player(data)
        self.assertEqual(player.player, 'LeBron James')
        self.assertEqual(player.team_id, 'LAL')
        self.assertEqual(player.pts, 22.0)
        self.assertEqual(player.date, '2025-11-21')

    def test_to_dict_returns_all_fields(self):
        """to_dict() returns dict with all player fields"""
        player = Player()
        player.id = '2025-11-21_LeBron James'
        player.player = 'LeBron James'
        player.team_id = 'LAL'
        player.opp_id = 'BOS'
        player.mp = '32:45'
        player.fg = 8.0
        player.fga = 15.0
        player.fg_pct = 0.533
        player.fg3 = 2.0
        player.fg3a = 5.0
        player.fg3_pct = 0.4
        player.ft = 4.0
        player.fta = 5.0
        player.ft_pct = 0.8
        player.orb = 1.0
        player.drb = 5.0
        player.trb = 6.0
        player.ast = 7.0
        player.stl = 1.0
        player.blk = 0.0
        player.tov = 2.0
        player.pts = 22.0
        player.plus_minus = 5.0
        player.date = '2025-11-21'

        result = player.to_dict()

        self.assertEqual(result['id'], '2025-11-21_LeBron James')
        self.assertEqual(result['player'], 'LeBron James')
        self.assertEqual(result['team_id'], 'LAL')
        self.assertEqual(result['pts'], 22.0)
        self.assertEqual(result['date'], '2025-11-21')
        # Check all keys are present
        self.assertEqual(
            set(result.keys()),
            {
                'id',
                'player',
                'team_id',
                'opp_id',
                'mp',
                'fg',
                'fga',
                'fg_pct',
                'fg3',
                'fg3a',
                'fg3_pct',
                'ft',
                'fta',
                'ft_pct',
                'orb',
                'drb',
                'trb',
                'ast',
                'stl',
                'blk',
                'tov',
                'pts',
                'plus_minus',
                'date',
            },
        )

    def test_to_dict_with_none_values(self):
        """to_dict() preserves None values"""
        data = {
            'id': 'test',
            'player': None,
            'team_id': 'TST',
            'opp_id': None,
            'mp': '20:00',
            'fg': None,
            'fga': 10.0,
            'fg_pct': None,
            'fg3': 1.0,
            'fg3a': 5.0,
            'fg3_pct': 0.2,
            'ft': None,
            'fta': 0.0,
            'ft_pct': None,
            'orb': 0.0,
            'drb': 2.0,
            'trb': 2.0,
            'ast': 3.0,
            'stl': None,
            'blk': 0.0,
            'tov': 1.0,
            'pts': None,
            'plus_minus': None,
            'date': '2025-11-21',
        }
        player = Player(data)

        result = player.to_dict()

        self.assertIsNone(result['player'])
        self.assertIsNone(result['pts'])
        self.assertEqual(result['id'], 'test')

    def test_from_dict_populates_all_fields(self):
        """from_dict() sets all player attributes from dict"""
        data = {
            'id': '2025-11-21_Kyrie Irving',
            'player': 'Kyrie Irving',
            'team_id': 'DAL',
            'opp_id': 'LAL',
            'mp': '28:30',
            'fg': 9.0,
            'fga': 18.0,
            'fg_pct': 0.5,
            'fg3': 3.0,
            'fg3a': 8.0,
            'fg3_pct': 0.375,
            'ft': 2.0,
            'fta': 2.0,
            'ft_pct': 1.0,
            'orb': 0.0,
            'drb': 3.0,
            'trb': 3.0,
            'ast': 8.0,
            'stl': 2.0,
            'blk': 0.0,
            'tov': 1.0,
            'pts': 23.0,
            'plus_minus': 10.0,
            'date': '2025-11-21',
        }
        player = Player()
        player.from_dict(data)

        self.assertEqual(player.id, '2025-11-21_Kyrie Irving')
        self.assertEqual(player.player, 'Kyrie Irving')
        self.assertEqual(player.team_id, 'DAL')
        self.assertEqual(player.ast, 8.0)
        self.assertEqual(player.pts, 23.0)

    def test_from_dict_with_none_values(self):
        """from_dict() handles None values"""
        data = {
            'id': 'test_id',
            'player': None,
            'team_id': 'TEST',
            'opp_id': None,
            'mp': '20:00',
            'fg': None,
            'fga': 10.0,
            'fg_pct': None,
            'fg3': 1.0,
            'fg3a': 5.0,
            'fg3_pct': 0.2,
            'ft': None,
            'fta': 0.0,
            'ft_pct': None,
            'orb': 0.0,
            'drb': 2.0,
            'trb': 2.0,
            'ast': 3.0,
            'stl': None,
            'blk': 0.0,
            'tov': 1.0,
            'pts': 5.0,
            'plus_minus': None,
            'date': '2025-11-21',
        }
        player = Player()
        player.from_dict(data)

        self.assertIsNone(player.player)
        self.assertIsNone(player.opp_id)
        self.assertIsNone(player.fg)
        self.assertEqual(player.team_id, 'TEST')

    def test_to_dict_from_dict_roundtrip(self):
        """Player data survives to_dict() -> from_dict() -> to_dict() cycle"""
        original_data = {
            'id': '2025-11-21_Giannis Antetokounmpo',
            'player': 'Giannis Antetokounmpo',
            'team_id': 'MIL',
            'opp_id': 'BOS',
            'mp': '34:12',
            'fg': 11.0,
            'fga': 22.0,
            'fg_pct': 0.5,
            'fg3': 1.0,
            'fg3a': 4.0,
            'fg3_pct': 0.25,
            'ft': 9.0,
            'fta': 12.0,
            'ft_pct': 0.75,
            'orb': 2.0,
            'drb': 8.0,
            'trb': 10.0,
            'ast': 5.0,
            'stl': 1.0,
            'blk': 2.0,
            'tov': 3.0,
            'pts': 32.0,
            'plus_minus': 8.0,
            'date': '2025-11-21',
        }

        player = Player(original_data)
        dict_result = player.to_dict()

        player2 = Player()
        player2.from_dict(dict_result)
        dict_result2 = player2.to_dict()

        self.assertEqual(dict_result, dict_result2)
        self.assertEqual(original_data, dict_result2)

    def test_str_format(self):
        """__str__() returns formatted player stats"""
        player = Player()
        player.player = 'Steph Curry'
        player.pts = 35.0
        player.ast = 10.0
        player.trb = 6.0

        result = str(player)

        self.assertEqual(result, 'Steph Curry (35.0/10.0/6.0)')

    def test_str_with_none_values(self):
        """__str__() handles None stat values gracefully"""
        player = Player()
        player.player = 'Unknown'
        player.pts = None
        player.ast = None
        player.trb = None

        result = str(player)

        # Should not raise; format includes None values
        self.assertIn('Unknown', result)


if __name__ == '__main__':
    unittest.main()