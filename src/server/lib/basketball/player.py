from pydantic import BaseModel, RootModel, Field
from typing import Optional

class BasePlayer(BaseModel):
    """ Player class for storing stats"""
    id: Optional[str] = None
    player: Optional[str] = Field(description='Player Name')
    team_id: Optional[str] = Field(description='Current Team Abbreviation (3 Letters)')
    opp_id: Optional[str] = Field(description='Opponent Team Abbreviation (3 Letters)')

class Player(BasePlayer):
    """ Player class for storing stats"""
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

def print_player(player: Player) -> str:
    """Print Player with format 'NAME (PTS/AST/TRB)'"""
    print(f"{player['player']} ({player['pts']}/{player['ast']}/{player['trb']})")


# Projection
class ProjectedPlayer(BaseModel):
    player: Player = Field(description='Player class for projected NBA player stats')
    num_games: int = Field(description="Number of upcoming games for this player's team.")
    opponents: list[str] = Field(description="List of team names of upcoming opponents for this player's team. Use the team name abbreviation or acronym")
    game_dates: list[str] = Field(description="List of dates for this player's upcoming games")
    analysis: str = Field(description="1-3 sentences describing the why the predicted stat line is accurate and recent trends")
    tags: list[str] = Field(description="List of applicable player tags", examples=["['minutes_up', 'stocks']", "['minutes_up']"])

class ProjectedPlayerList(RootModel[list[ProjectedPlayer]]):
    pass

def print_projected_player(projectedPlayer: ProjectedPlayer, actualPlayer: Player = None):
    """Print Player name and projected stats"""
    player: Player = projectedPlayer['player']

    labels = ['FG%', 'FT%', 'PTS', '3PM', 'REB', 'AST', 'STL', 'BLK', 'TOV']
    fields = ['fg_pct', 'ft', 'pts', 'fg3', 'trb', 'ast', 'stl', 'blk', 'tov']
    
    print(player['player'])
    if actualPlayer:
        print('Average Stats:')
        for label, field in zip(labels, fields):
            print(f'\t{label}: {actualPlayer[field]}')

    print('Predicted Stats:')
    for label, field in zip(labels, fields):
        print(f'\t{label}: {player[field]}')

    print(f'# of Upcoming Games:\n\t{projectedPlayer['num_games']}')
    print(f'Upcoming Opponents:\n\t{projectedPlayer['opponents']}')
    print(f'Upcoming Games:\n\t{projectedPlayer['game_dates']}')
    print(f'Analysis:\n\t{projectedPlayer['analysis']}')

# Trennding 
class TrendingPlayer(BaseModel):
    player: BasePlayer = Field(description='Player class for projected NBA player stats')
    num_games: int = Field(description="Number of upcoming games for this player's team.")
    opponents: list[str] = Field(description="List of team names of upcoming opponents for this player's team. Use the team name abbreviation or acronym")
    game_dates: list[str] = Field(description="List of dates for this player's upcoming games")
    analysis: str = Field(description="1-3 sentences describing the why the predicted stat line is accurate and recent trends")
    tags: list[str] = Field(description="List of one ore more player tags where 'minutes_up' = an increase in minutes, 'stocks' = an high steal and/or block total", examples=['minutes_up', 'stocks'])
    
class TrendingPlayerList(RootModel[list[TrendingPlayer]]):
    pass

def print_trending_player(projectedPlayer: TrendingPlayer, actualPlayer: Player = None):
    """Print Player name and projected stats"""
    player: Player = projectedPlayer['player']

    labels = ['FG%', 'FT%', 'PTS', '3PM', 'REB', 'AST', 'STL', 'BLK', 'TOV']
    fields = ['fg_pct', 'ft', 'pts', 'fg3', 'trb', 'ast', 'stl', 'blk', 'tov']
    
    print(player['player'])
    if actualPlayer:
        print('Average Stats:')
        for label, field in zip(labels, fields):
            print(f'\t{label}: {actualPlayer[field]}')

    print(f'# of Upcoming Games:\n\t{projectedPlayer['num_games']}')
    print(f'Upcoming Opponents:\n\t{projectedPlayer['opponents']}')
    print(f'Upcoming Games:\n\t{projectedPlayer['game_dates']}')
    print(f'Analysis:\n\t{projectedPlayer['analysis']}')