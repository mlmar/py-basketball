# py-basketball

Objectives

- [ ] Frontend
  - Libraries
    - [ ] [React](https://react.dev/learn)
    - [ ] [TypeScript](typescriptlang.org/cheatsheets/)
    - [ ] [@tanstack/tanstack-router](https://tanstack.com/router/latest)
    - [ ] [@tanstack/query](https://tanstack.com/query/latest)
    - [ ] [zustand](https://github.com/pmndrs/zustand)
  - [ ] Yahoo API
    - [ ] Prompt user for login
    - [ ] Show list of trending players based on league settings
  - [ ] Generic
    - [ ] Watching players (tracking trends for specific player)
    - [ ] Show list of trending players (top performing based on criteria) in the NBA
    - [ ] Watching players (tracking trends for specific player)
- [ ] Backend
  - [ ] Selenium
    - [x] Scrape data from [basketball-reference](https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=11&day=17&year=2025)
  - [x] External Services
    - [x] Retrieve upcoming NBA schedule for the next N days
    - [x] Retrieve player stats from NBA API
  - [x] Supabase
    - [x] player_data table - Saved player statistics
    - [x] saved_dates table - Indicates which dates have already been scraped
    - [x] Supabase functions for grabbing all/average/totals of player stats from the last N days
  - [ ] Use AI to analyse player data and create projects
    - [x] Google Gemini
      - [ ] Determine work around for January 2025 knowledge cut off
      - [ ] Feed entire season data set for all players and schedule (Will need to workaround API Limits)
        - [ ] Use different AI API?
    - [x] Feed statistics from the last N days
    - [x] Get projected statistics for the next N days
    - [x] Incorporate upcoming NBA schedule
      - [x] Get number of games for next N days
      - [x] Get list of opponents for next N days
  - [ ] Automation
    - [ ] Automate daily/weekly analysis for N days
    - [ ] Pull data once per day and cache pervious analysis results
  - [ ] fastapi routes for:
    - [ ] Authentication -- require Supabase JWT token to access routes
    - [ ] Serving front end application
    - [ ] Accessing player statistics
      - [x] Projected players for the next N days
      - [x] Player averages from last N days
      - [ ] Trending players from last N days
    - [ ] Passing specific criteria for analysis
      - [ ] Dependent on API rate limits (Too much data?)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r src/server/requirements.txt
pip install
npm install --prefix ./src/client
```

Create an .env file in the server directory with the folllowing contents:

```properties
SUPABASE_URL=YOUR_SUPABASE_URL_HERE
SUPABASE_KEY=YOUR_SUPABASE_KEY_HERE
SUPABASE_SAVED_DATES_TABLE=YOUR_SUPABASE_SAVED_DATES_TABLE_HERE
SUPABASE_PLAYER_DATA_TABLE=YOUR_SUPABASE_PLAYER_DATA_TABLE_HERE
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
PYTHONPATH=./src/server
```

Supabase connection strings are required for authentication and data retrieval.

## Run Server

Makefile Support

```bash
cd src/server
make run
```

Or

```bash
cd src/server
pip install -r requirements.txt
fastapi dev main.py --port 3300
```

## Run Client

```bash
cd src/client
npm run dev
```
