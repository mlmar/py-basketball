from nba_api.stats.endpoints import LeagueGameLog, BoxScoreTraditionalV3
import time
from lib.basketball.player import Player, print_player
from typing import Generator
from datetime import date

SEASON = '2025-26'

def __get_players(current_date: date):
    games_df = LeagueGameLog(
        season=SEASON,
        season_type_all_star='Regular Season'
    ).get_data_frames()[0]

    games_df = games_df[games_df['GAME_DATE'] == str(current_date)]
    game_ids = games_df['GAME_ID'].unique()

    all_players: Player = []

    for game_id in game_ids:
        print('Fetching game:', game_id)

        boxscore = BoxScoreTraditionalV3(game_id=game_id).get_data_frames()[0]
        for index, item in enumerate(boxscore['gameId']):
            data = boxscore.iloc[index].to_dict();
            player: Player = __parse_table_row(data, current_date)
            all_players.append(player)

        time.sleep(0.6)  # NBA API rate limit protection
    
    return all_players

def __parse_table_row(row, current_date: date) -> Player:
    """Parses NBA box score row"""
    player: Player = {};
    player['player'] = f'{row['firstName']} {row['familyName']}';
    player['team_id'] = row['teamTricode']
    player['mp'] = row['minutes']
    player['fg'] = row['fieldGoalsMade']
    player['fga'] = row['fieldGoalsAttempted']
    player['fg_pct'] = row['fieldGoalsPercentage']
    player['fg3'] = row['threePointersMade']
    player['fg3a'] = row['threePointersAttempted']
    player['fg3_pct'] = row['threePointersPercentage']
    player['ft'] = row['freeThrowsMade']
    player['fta'] = row['freeThrowsAttempted']
    player['ft_pct'] = row['freeThrowsPercentage']
    player['orb'] = row['reboundsOffensive']
    player['drb'] = row['reboundsDefensive']
    player['trb'] = row['reboundsTotal']
    player['ast'] = row['assists']
    player['stl'] = row['steals']
    player['blk'] = row['blocks']
    player['tov'] = row['turnovers']
    player['pts'] = row['points']
    player['plus_minus'] = row['plusMinusPoints']
    player['date'] = str(current_date)
    player['id'] = f'{str(player['date'])}_{player['player']}'
    return player;

# Fetch page at base url
def get_data(dates: list[date] = []) -> Generator[(date, list[Player])]:
    """Fetches data from basketball reference for a range of dates"""

    if len(dates) == 0:
        return

    start_date = dates[0]
    end_date = dates[-1]
    print(f'Fetching data from {start_date} to {end_date}')

    # Fetch data for range of dates
    for current_date in dates:
        players: list[Player] = __get_players(current_date);
        yield (current_date, players)
            
    print(f'Successfully fetched data from {start_date} to {end_date}')