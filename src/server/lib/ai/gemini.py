import json
from datetime import date
from lib.ai.client import get_client
from lib.basketball.player import Player, ProjectedPlayerList, print_projected_player
from service.nba_cdn_service import get_nba_schedule
from google.genai import types

def get_analysis(data: list[Player], type: str, days: int):
    prompt = f"""
    Today is {str(date.today())}.
    The first data set contains NBA players and their {type} from the last {days} days. 
    The second data set contains the NBA game schedule for remainder of the season.
    Determine the 10 most underrated players based on this data set, and prioritize non all stars.
    For each underrated player, project or determine the following for the next 7 days: (
        Project their average stats where:
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
        num_games = Based on the provided NBA game schedule data set, determine the number of upcoming games for this player's team.
        opponents = Based on the provided NBA game schedule data set, determine the exact list of team names of upcoming opponents for this player's team. Use the team name abbreviation or acronym.
        game_dates = Based on the provided NBA game schedule data set, determine the exact list of dates for this player's upcoming games
    
    )
    Respond in valid JSON format without new line characters.
    """

    client = get_client()
    nba_schedule = get_nba_schedule(date.today())

    print(prompt)
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

    final_answer = ''
    # Print out response stream thoughts
    for chunk in response_stream:
        if chunk.candidates[0].content.parts != None:
            for part in chunk.candidates[0].content.parts:
                if part.text:
                    if part.thought:
                        print(f'[Thinking]: {part.text}', end='\n', flush=True)
                    else:
                        final_answer += part.text
                        print(f'{part.text}', end='', flush=True)

    print('\n\n------ Projections for underrated players for the next 7 days ------\n')
    result: ProjectedPlayerList = json.loads(final_answer)
    for projectedPlayer in result:
        print_projected_player(projectedPlayer)
        print()