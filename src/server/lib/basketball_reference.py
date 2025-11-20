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
from pydantic import BaseModel
from datetime import date
from util.date_util import range_of_dates

class PlayerData(BaseModel):
    name: str
    team: str
    opponent: str
    minutes_played: str
    fg_made: float
    fg_attempted: float
    fg_pct: float
    fg_3_made: float
    fg_3_attempted: float
    fg_3_pct: float
    ft_made: float
    ft_attempted: float
    ft_pct: float
    orb: float
    drb: float
    trb: float
    assists: float
    steals: float
    blocks: float
    turnovers: float
    points: float
    plus_minus: float

_row_data_mapping = {
    "name": "player",
    "team": "team_id",
    "opponent": "opp_id",
    "minutes_played": "mp",
    "fg_made": "fg",
    "fg_attempted": "fga",
    "fg_pct": "fg_pct",
    "fg_3_made": "fg3",
    "fg_3_attempted": "fg3a",
    "fg_3_pct": "fg3_pct",
    "ft_made": "ft",
    "ft_attempted": "fta",
    "ft_pct": "ft_pct",
    "orb": "orb",
    "drb": "drb",
    "trb": "trb",
    "assists": "ast",
    "steals": "stl",
    "blocks": "blk",
    "turnovers": "tov",
    "pointsts": "pts",
    "plus_minus": "plus_minus"
}

# Retrieve base url
def get_url(date: date) -> str:
    """Returns url to basketball reference stats page for todays date"""

    return f'https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=${date.month}&day={date.day}&year={date.year}'

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

# Parses html td element table row into a PlayerData object
def __parse_table_row(row: WebElement) -> PlayerData:
    """Parses a single table row into a PlayerData object from basketball reference stats table"""

    playerData: PlayerData = {}
    for key in _row_data_mapping:
        playerData[key] = row.find_element(By.CSS_SELECTOR, f'[data-stat={_row_data_mapping[key]}]').get_attribute('innerText')
    return playerData

def __parse_table_rows(driver: WebDriver) -> list[PlayerData]:
    """Parses table rows into a list of PlayerData from basketball reference stats page"""

    rows = driver.find_elements(By.CSS_SELECTOR, '[data-row]')
    players: list[PlayerData] = [__parse_table_row(row) for row in rows]
    return players

# Fetch page at base url
def get_data(start_date: date, end_date: date) -> Generator[PlayerData]:
    """Fetches data from basketball reference for a range of dates"""

    if start_date > end_date:
        raise Exception('start_date must be before end_date') 
    
    print(f'Fetching data from {start_date} to {end_date}')

    print('Creating driver')
    driver = __create_driver()
    wait = WebDriverWait(driver, 10)

    # Fetch data for range of dates
    for current_date in range_of_dates(start_date, end_date):
        url = get_url(current_date)

        print(f'Fetching data from {url}')
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-row]'))) # Wait until top 20 rows of table are loaded
        
        print(f'Waiting until table rows are present')
        
        print('Querying data from table rows')
        yield __parse_table_rows(driver)
            
    driver.quit()
    print(f'Successfully fetched data from {start_date} to {end_date}')