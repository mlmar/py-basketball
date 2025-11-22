from pydantic import BaseModel, RootModel, Field
from typing import Optional

class Player(BaseModel):
    """ Player class for storing stats from basketball reference"""
    id: Optional[str] = None
    player: Optional[str] = Field(description='Player Name')
    team_id: Optional[str] = Field(description='Current Team Abbreviation (3 Letters)')
    opp_id: Optional[str] = Field(description='Opponent Team Abbreviation (3 Letters)')
    mp: Optional[str] = Field(description='Minutes played')
    fg: Optional[float] = Field(description='Field Goals Made')
    fga: Optional[float] = Field(description='Field Goals Attempted')
    fg_pct: Optional[float] = Field(description='Field Goal Percentage in decimal format')
    fg3: Optional[float] = Field(description='Three Pointers Made')
    fg3a: Optional[float] = Field(description='Three Pointers Attempted')
    fg3_pct: Optional[float] = Field(description='Three Pointers Percentage in decimal format')
    ft: Optional[float] = Field(description='Free Throws Made')
    fta: Optional[float] = Field(description='Free Throws Attempted')
    ft_pct: Optional[float] = Field(description='Free Throw Percentage in decimal format')
    orb: Optional[float] = Field(description='Offensive Rebounds')
    drb: Optional[float] = Field(description='Defensive Rebounds')
    trb: Optional[float] = Field(description='Total Rebounds (Offensive Rebounds + Defensive Rebounds)')
    ast: Optional[float] = Field(description='Assists')
    stl: Optional[float] = Field(description='Steals')
    blk: Optional[float] = Field(description='Blocks')
    tov: Optional[float] = Field(description='Turnovers')
    pts: Optional[float] = Field(description='Points')
    plus_minus: Optional[float] = Field(description='Plus Minus')
    date: Optional[str] = None

class ProjectedPlayer(BaseModel):
    player: Player = Field(description='Player class for projected NBA player stats')
    num_games: int = Field(description="Number of upcoming games for this player's team.")
    opponents: list[str] = Field(description="List of team names of upcoming opponents for this player's team. Use the team name abbreviation or acronym")
    game_dates: list[str] = Field(description="List of dates for this player's upcoming games")

class ProjectedPlayerList(RootModel[list[ProjectedPlayer]]):
    pass

def print_player(player: Player) -> str:
    """Print Player with format 'NAME (PTS/AST/TRB)'"""
    return f"{player['name']} ({player['pts']}/{player['ast']}/{player['trb']})"

def print_projected_player(projectedPlayer: ProjectedPlayer):
    """Print Player name and projected stats"""
    player: Player = projectedPlayer['player']

    labels = ['FG%', 'FT%', 'PTS', '3PM', 'REB', 'AST', 'STL', 'BLK', 'TOV']
    fields = ['fg_pct', 'ft', 'pts', 'fg3', 'trb', 'ast', 'stl', 'blk', 'tov']
    
    print(player['player'])
    for label, field in zip(labels, fields):
        print(f'\t{label}: {player[field]}')

    print(f'\t# of Upcoming Games: {projectedPlayer['num_games']}')
    print(f'\tUpcoming Opponents: {projectedPlayer['opponents']}')
    print(f'\tUpcoming Games: {projectedPlayer['game_dates']}')