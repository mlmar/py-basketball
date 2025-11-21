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
    
    def __init__(self,
        player: str = None,
        team_id: str = None,
        opp_id: str = None,
        mp: str = None,
        fg: float = None,
        fga: float = None,
        fg_pct: float = None,
        fg3: float = None,
        fg3a: float = None,
        fg3_pct: float = None,
        ft: float = None,
        fta: float = None,
        ft_pct: float = None,
        orb: float = None,
        drb: float = None,
        trb: float = None,
        ast: float = None,
        stl: float = None,
        blk: float = None,
        tov: float = None,
        pts: float = None,
        plus_minus: float = None):
        
        self.player = player
        self.team_id = team_id
        self.opp_id = opp_id
        self.mp = mp
        self.fg = fg
        self.fga = fga
        self.fg_pct = fg_pct
        self.fg3 = fg3
        self.fg3a = fg3a
        self.fg3_pct = fg3_pct
        self.ft = ft
        self.fta = fta
        self.ft_pct = ft_pct
        self.orb = orb
        self.drb = drb
        self.trb = trb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tov = tov
        self.pts = pts
        self.plus_minus = plus_minus

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
    
    def __str__(self):
        return f'{self.player} ({self.pts}/{self.ast}/{self.trb})'