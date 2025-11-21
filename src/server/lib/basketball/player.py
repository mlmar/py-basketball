from datetime import date

class Player:
    """ Player class for storing stats from basketball reference"""
    id: str
    player: str
    team_id: str
    opp_id: str
    mp: str
    fg: float
    fga: float
    fg_pct: float
    fg3: float
    fg3a: float
    fg3_pct: float
    ft: float
    fta: float
    ft_pct: float
    orb: float
    drb: float
    trb: float
    ast: float
    stl: float
    blk: float
    tov: float
    pts: float
    plus_minus: float
    
    def __init__(self, playerDict = None):
        if playerDict != None:
            self.from_dict(playerDict)


    def to_dict(self) -> dict:
        """Converts Player to dict object"""
        return {
            'id': self.id, 
            'player': self.player, 
            'team_id': self.team_id, 
            'opp_id': self.opp_id, 
            'mp': self.mp, 
            'fg': self.fg, 
            'fga': self.fga, 
            'fg_pct': self.fg_pct, 
            'fg3': self.fg3, 
            'fg3a': self.fg3a, 
            'fg3_pct': self.fg3_pct, 
            'ft': self.ft, 
            'fta': self.fta, 
            'ft_pct': self.ft_pct, 
            'orb': self.orb, 
            'drb': self.drb, 
            'trb': self.trb, 
            'ast': self.ast, 
            'stl': self.stl, 
            'blk': self.blk, 
            'tov': self.tov, 
            'pts': self.pts, 
            'plus_minus': self.plus_minus
        }
    
    def from_dict(self, playerDict):
        self.player = playerDict['player']
        self.team_id = playerDict['team_id']
        self.opp_id = playerDict['opp_id']
        self.mp = playerDict['mp']
        self.fg = playerDict['fg']
        self.fga = playerDict['fga']
        self.fg_pct = playerDict['fg_pct']
        self.fg3 = playerDict['fg3']
        self.fg3a = playerDict['fg3a']
        self.fg3_pct = playerDict['fg3_pct']
        self.ft = playerDict['ft']
        self.fta = playerDict['fta']
        self.ft_pct = playerDict['ft_pct']
        self.orb = playerDict['orb']
        self.drb = playerDict['drb']
        self.trb = playerDict['trb']
        self.ast = playerDict['ast']
        self.stl = playerDict['stl']
        self.blk = playerDict['blk']
        self.tov = playerDict['tov']
        self.pts = playerDict['pts']
        self.plus_minus = playerDict['plus_minus']
    
    def __str__(self):
        return f'{self.player} ({self.pts}/{self.ast}/{self.trb})'