import json
# from unicodedata import normalize
from datetime import date
from lib.ai.client import get_client
from lib.basketball.player import Player, ProjectedPlayerList, print_projected_player
from service.nba_cdn_service import get_nba_schedule
from google.genai import types

def get_analysis(data: list[Player], past_days: int, num_players: int = 5, future_days: int = 7):
    prompt = f"""
    Today is {str(date.today())}.
    Here are 2 data sets:
        The first data set contains NBA players and their statlines from the last {past_days} days. 
        The second data set contains the NBA game schedule for remainder of the season.

    Determine a list of the {num_players} most underrated players based on these data sets,
    and accurately project their average stats over the next {future_days} days.
    Accurately generate new data based on these requirements. Do not simply take the average of the last 10 days.
    Consider the statlines of each player from the last {past_days} days from the first data set in comparison to their career stats.
    Consider their number upcoming of games and the difficulty of upcoming opponents from the second data set.
    Prioritize non all stars.

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

    Third:
    Respond in valid JSON format without new line characters.
    """

    print(prompt)
    response_stream = __get_gemini_response(data, prompt)
    result, final_answer = __parse_response_stream(response_stream)
    __print_projected_players(result)
    return result

def get_projected_analysis(data: list[Player], past_days: int, num_players: int = 10, future_days: int = 7):
    """Projects stats for underrated players for the next N days"""
    
    prompt = f"""
    Today is {str(date.today())}.
    Here are 2 data sets:
        The first data set contains NBA players and their statlines from the last {past_days} days. 
        The second data set contains the NBA game schedule for remainder of the season.

    Determine a list of the {num_players} most underrated players based on these data sets,
    and accurately project their average stats over the next {future_days} days.
    Accurately generate new data based on these requirements. Do not simply take the average of the last 10 days.
    Consider the statlines of each player from the last {past_days} days from the first data set in comparison to their career stats.
    Consider their number upcoming of games and the difficulty of upcoming opponents from the second data set.
    Prioritize non all stars.

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

    Third:
    Respond in valid JSON format without new line characters.
    """

    print(prompt)
    client = get_client()
    nba_schedule = get_nba_schedule(date.today())
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
    __print_projected_players(result)
    return result

def get_trending_analysis(data: list[Player], past_days: int, num_players: int = 20, future_days: int = 7):
    """Determines the top trending players from the last N, calcualtes their average stats and determines their game schedule for the next X days"""

    prompt = f"""
    Today is {str(date.today())}.
    Here are 2 data sets:
        The first data set contains NBA players and their statlines from the last {past_days} days. 
        The second data set contains the NBA game schedule for remainder of the season.

    Determine a list of the top {num_players} performing players from the last {past_days} days, excluding all stars.

    Format the upcoming games for the next {future_days} days as follows:
        num_games = Based on the provided NBA game schedule data set, the number of upcoming games for this player's team.
        opponents = Based on the provided NBA game schedule data set, the exact list of team names of upcoming opponents for this player's team. Use the team name abbreviation or acronym.
        game_dates = Based on the provided NBA game schedule data set, the exact list of dates for this player's upcoming games

    analysis = 1-3 sentences describing the why the player is trending

    Third:
    Respond in valid JSON format without new line characters.
    """

    print(prompt)

    client = get_client()
    nba_schedule = get_nba_schedule(date.today())
    response_stream = client.models.generate_content_stream(
        model='gemini-2.5-flash',
        contents=[
            json.dumps(data),
            prompt
        ],
        config={
            "response_mime_type": "application/json",
            "response_json_schema": ProjectedPlayerList.model_json_schema(),
            "thinking_config": types.ThinkingConfig(include_thoughts=True)
        },
    )

    result, final_answer = __parse_response_stream(response_stream)
    __print_projected_players(result)
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

def __print_projected_players(projected_players: ProjectedPlayerList):
    for projected_player in projected_players:
        # Find actual player by normalizing it and comparing it to original list
        # actualPlayer = next((x for x in data if normalize('NFD', x['player']) == normalize('NFD', projected_player['player']['player'])), None)
        print_projected_player(projected_player)
        print()