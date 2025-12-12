import json
# from unicodedata import normalize
from datetime import date
import config
from lib.ai.client import get_client
from lib.basketball.player import Player, ProjectedPlayerList, print_projected_player, TrendingPlayerList, print_trending_player
from service.nba_cdn_service import get_nba_schedule
from google.genai import types
from util.date_util import get_today_pst

def get_projected_analysis(data: list[Player], past_days: int, num_players: int = 10, future_days: int = 7):
    """Projects stats for underrated players for the next N days"""
    
    prompt = f"""
    Today is {str(get_today_pst())}.
    You are given two data sets:
    1) DataSetA: NBA player statlines from the last {past_days} days.
    2) DataSetB: NBA game schedule for the next {future_days} days.

    Task:
    - Identify the {num_players} most underrated players based on both data sets.
    - Generate NEW projected averages for each player over the next {future_days} days.
    - Do NOT simply average recent stats. Instead:
        - Compare recent performance to career norms.
        - Factor in pace, usage, role/minutes changes, and efficiency trends.
        - Consider schedule difficulty and number of games from DataSetB.
    - Order and rank the resulting players from 1 to {num_players} where 1 is the best player

    Upcoming Games (from DataSetB):
    - num_games: Number of games their team plays in the next {future_days}.
    - opponents: Opponent team abbreviations.
    - game_dates: Exact dates of those games.

    Projected Stats (averages over next {future_days} days), with meanings:
    mp = Minutes played
    fg = Field goals made
    fga = Field goals attempted
    fg_pct = FG% (decimal)
    fg3 = 3-pointers made
    fg3a = 3-pointers attempted
    fg3_pct = 3P% (decimal)
    ft = Free throws made
    fta = Free throws attempted
    ft_pct = FT% (decimal)
    orb = Offensive rebounds
    drb = Defensive rebounds
    trb = Total rebounds
    ast = Assists
    stl = Steals
    blk = Blocks
    tov = Turnovers
    pts = Points
    plus_minus = Plus/minus

    analysis:
    1-3 concise sentences explaining why the projection is realistic (recent trends, minutes/role changes, efficiency, schedule difficulty, do NOT mention fantasy points).

    tags:
    Include all applicable tags:
    - "minutes_up" = Increased in minutes expected
    - "stocks" = High steals or blocks expected

    rank:
    - Order and rank the resulting players from 1 to {num_players} where 1 is the best player

    Output:
    Return ONLY minified JSON with no spaces or new lines.
    """

    print(prompt)
    client = get_client()
    nba_schedule = get_nba_schedule(get_today_pst(), future_days)
    response_stream = client.models.generate_content_stream(
        model='gemini-2.5-flash',
        contents=[
            json.dumps(data),
            json.dumps(nba_schedule),
            prompt
        ],
        config={
            "response_mime_type": "application/json",
            "response_json_schema": ProjectedPlayerList.model_json_schema(),
            "thinking_config": types.ThinkingConfig(include_thoughts=True)
        },
    )
    result, final_answer = __parse_response_stream(response_stream)
    for projected_player in result:
        # Find actual player by normalizing it and comparing it to original list
        # actualPlayer = next((x for x in data if normalize('NFD', x['player']) == normalize('NFD', projected_player['player']['player'])), None)
        print_projected_player(projected_player)
        print()
    return result

def get_trending_analysis(data: list[Player], past_days: int, num_players: int = config.ANALYSIS_PLAYER_LIMIT, future_days: int = 7):
    """Determines the top trending players from the last N, calcualtes their average stats and determines their game schedule for the next X days"""

    prompt = f"""
    Today is {str(get_today_pst())}.
    Here are two data sets:
    1) DataSetA: NBA player statlines from the last {past_days} days.
    2) DataSetB: NBA game schedule for the next {future_days} days.

    Task:
    - Identify the top {num_players} performers from DataSetA based on recent production over the last {past_days} days.

    For each selected player, use DataSetB to determine:
    - num_games: Number of upcoming games for the player's team.
    - opponents: List of opponent team abbreviations for those games.
    - game_dates: List of game dates for those matchups.

    analysis:
    - Provide 2-3 short phrases (<10 words each, comma-separated) explaining why the player is trending.
    - Can include averages, notable stats, role changes, etc.
    Examples:
    - "Last 3: 22 PTS, 4 REB, 3.7 3PM",
    - "Stuffing stocks: 2.2 STL, 1.5 BLK recently",
    - "Efficient big: 64% FG, solid boards",
    - "Injury replacement getting starter run"

    tags:
    Include all applicable tags:
    - "minutes_up" = Increase in minutes
    - "stocks" = High steals or blocks

    rank:
    - Order and rank the resulting players from 1 to {num_players} where 1 is the best player
    
    Output:
    Return ONLY minified JSON with no spaces or new lines.
    """

    print(prompt)

    client = get_client()
    nba_schedule = get_nba_schedule(get_today_pst(), future_days)
    response_stream = client.models.generate_content_stream(
        model='gemini-2.5-flash',
        contents=[
            json.dumps(data),
            json.dumps(nba_schedule),
            prompt
        ],
        config={
            "response_mime_type": "application/json",
            "response_json_schema": TrendingPlayerList.model_json_schema(),
            "thinking_config": types.ThinkingConfig(include_thoughts=True)
        },
    )

    result, final_answer = __parse_response_stream(response_stream)
    for projected_player in result:
        # Find actual player by normalizing it and comparing it to original list
        # actualPlayer = next((x for x in data if normalize('NFD', x['player']) == normalize('NFD', projected_player['player']['player'])), None)
        print_trending_player(projected_player)
        print()
    
    return result

def __parse_response_stream(response_stream) -> tuple[dict, str]:
    """
    Parses gemini response stream.
    Prints thoughts and answers and returns final answer as (json, str) tuple
    """
    final_answer = ''
    # Print out response stream thoughts
    for chunk in response_stream:
        if chunk.candidates[0].content.parts is not None:
            for part in chunk.candidates[0].content.parts:
                if part.text:
                    if part.thought:
                        print(f'[Thinking]: {part.text}', end='\n', flush=True)
                    else:
                        final_answer += part.text
                        print(f'{part.text}', end='', flush=True)

    return (json.loads(final_answer), final_answer)