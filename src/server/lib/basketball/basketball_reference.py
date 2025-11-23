# https://www.selenium.dev/documentation/
# File for scraping data from https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=11&day=17&year=2025

from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from datetime import date
from lib.basketball.player import Player

# Types matching
_row_data_stat_types = {
    "player": str,
    "team_id": str,
    "opp_id": str,
    "mp": str,
    "fg": float,
    "fga": float,
    "fg_pct": float,
    "fg3": float,
    "fg3a": float,
    "fg3_pct": float,
    "ft": float,
    "fta": float,
    "ft_pct": float,
    "orb": float,
    "drb": float,
    "trb": float,
    "ast": float,
    "stl": float,
    "blk": float,
    "tov": float,
    "pts": float,
    "plus_minus": float
}

# Retrieve base url
def get_url(date: date = None) -> str:
    """Returns url to basketball reference stats page for todays date"""

    if date == None:
        raise Exception('Date cannot be None')

    return f'https://www.basketball-reference.com/friv/dailyleaders.fcgi?month={date.month}&day={date.day}&year={date.year}&type=all'

# Create driver with necessary parameters
def __create_driver() -> WebDriver:
    """Creates headless Chrome webdriver"""

    arguments = [
        '--headless=new'
        '--disable-gpu'  # Recommended for headless mode
        '--disable-renderer-backgrounding'
        '--disable-background-timer-throttling'
        '--disable-backgrounding-occluded-windows'
        '--disable-dev-shm-usage'  # Helps with resource limits
        '--no-sandbox'  # Try if running in a containerized environment
    ]
    
    options = Options()
    options.page_load_strategy = 'none'
    for arg in arguments:
        options.add_argument(arg)

    driver = webdriver.Chrome(options=options)
    return driver

# Parses html td element table row into a Player object
def __parse_table_row(row: WebElement, current_date: date) -> Player:
    """Parses a single table row into a Player object from basketball reference stats table"""

    player: Player = {}
    for key in _row_data_stat_types:
        value = row.find_element(By.CSS_SELECTOR, f'td[data-stat={key}]').get_attribute('innerText')
        type = _row_data_stat_types[key]
        if value == '':
            value = None
        else:
            value = type(value)
        player[key] = value
    player['id'] = f'{str(current_date)}_{player['player']}'
    player['date'] = str(current_date)
    return player

def __parse_table_rows(driver: WebDriver, current_date: date, num: int = 100) -> list[Player]:
    """Parses top N table rows into a list of Player from basketball reference stats page"""

    rows = driver.find_elements(By.CSS_SELECTOR, '#all_stats tbody > tr[data-row]:not(.thead)')
    if len(rows) == 0:
        return []
    
    print(f'Queried {len(rows)} rows from stats table')
    players: list[Player] = [__parse_table_row(row, current_date) for row in rows]
    return players

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
        print(f'------ {current_date} ------')
        url = get_url(current_date)

        print(f'Fetching data from {url}')
        driver = __create_driver()
        try:
            wait = WebDriverWait(driver, 10)
            driver.get(url)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#all_stats'))) # Wait until top 20 rows of table are loaded
        except TimeoutException:
            print(f'No data found for {current_date}')
            yield (current_date, None)
            continue
        
        print(f'Querying data from table rows')
        players = __parse_table_rows(driver, current_date)
        print(f'Successfully fetched data for {len(players)} players')
        driver.quit()
        yield (current_date, players)
            
    print(f'Successfully fetched data from {start_date} to {end_date}')