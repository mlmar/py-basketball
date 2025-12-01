import json
# from unicodedata import normalize
from datetime import date
from lib.ai.client import get_client
from lib.basketball.player import Player, ProjectedPlayerList, print_projected_player, TrendingPlayerList, print_trending_player
from service.nba_cdn_service import get_nba_schedule
from google.genai import types

def get_projected_analysis(data: list[Player], past_days: int, num_players: int = 10, future_days: int = 7):
    """Projects stats for underrated players for the next N days"""
    
    prompt = f"""
    Today is {str(date.today())}.
    Here are 2 data sets:
        The first data set contains NBA players and their statlines from the last {past_days} days. 
        The second data set contains the NBA game schedule for the next {future_days} days.

    Determine a list of the {num_players} most underrated players based on these data sets,
    and accurately project their average stats over the next {future_days} days.
    Accurately generate new data based on these requirements. Do not simply take the average of the last 10 days.
    Consider the statlines of each player from the last {past_days} days from the first data set in comparison to their career stats.
    Consider their number upcoming of games and the difficulty of upcoming opponents from the second data set.

    Format the upcoming games for the next {future_days} days as follows:
        num_games = Based on the provided NBA game schedule data set, the number of upcoming games for this player's team.
        opponents = Based on the provided NBA game schedule data set, the exact list of team names of upcoming opponents for this player's team. Use the team name abbreviation or acronym.
        game_dates = Based on the provided NBA game schedule data set, the exact list of dates for this player's upcoming games

    The newly generated stats should be formatted as follows:
        mp = Minutes played
        fg = Field Goals Made
        fga = Field Goals Attempted
        fg_pct = Field Goal Percentage in decimal format
        fg3 = Three Pointers Made
        fg3a = Three Pointers Attempted
        fg3_pct = Three Pointers Percentage in decimal format
        ft = Free Throws Made
        fta = Free Throws Attempted
        ft_pct = Free Throw Percentage in decimal format
        orb = Offensive Rebounds
        drb = Defensive Rebounds
        trb = Total Rebounds (Offensive Rebounds + Defensive Rebounds)
        ast = Assists
        stl = Steals
        blk = Blocks
        tov = Turnovers
        pts = Points
        plus_minus = Plus Minus 

    analysis = 1-3 sentences describing the why the predicted stat line is accurate and recent trends
    tags = List of player tags where 'minutes_up' = an increase in minutes, 'stocks' = an high steal and/or block total

    Respond in minified JSON format without spaces and new lines.
    """

    print(prompt)
    client = get_client()
    nba_schedule = get_nba_schedule(date.today(), future_days)
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

def get_trending_analysis(data: list[Player], past_days: int, num_players: int = 20, future_days: int = 7):
    """Determines the top trending players from the last N, calcualtes their average stats and determines their game schedule for the next X days"""

    prompt = f"""
    Today is {str(date.today())}.
    Here are 2 data sets:
        The first data set contains NBA players and their statlines from the last {past_days} days. 
        The second data set contains the NBA game schedule for the next {future_days} days.

    Determine a list of the top {num_players} performing players from the last {past_days} days.

    Format the upcoming games for the next {future_days} days as follows:
        num_games = Based on the provided NBA game schedule data set, the number of upcoming games for this player's team.
        opponents = Based on the provided NBA game schedule data set, the exact list of team names of upcoming opponents for this player's team. Use the team name abbreviation or acronym.
        game_dates = Based on the provided NBA game schedule data set, the exact list of dates for this player's upcoming games

    analysis = 2-3 quick and short phrases describing why the player is trending (less than 10 words, comma separated, may include average or notable stats)
    Here are 4 examples of ways to phrase the analysis:
        "Last 3: 22 PTS, 4 REB, 3.7 3PM",
        "Stuffing stocks: 2.2 STL, 1.5 BLK recently"
        "Efficient big: 64% FG, solid boards"
        "Injury replacement getting starter run"

    tags = List of player tags where 'minutes_up' = an increase in minutes, 'stocks' = an high steal and/or block total

    Respond in minified JSON format without spaces and new lines.
    """

    print(prompt)

    client = get_client()
    nba_schedule = get_nba_schedule(date.today(), future_days)
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