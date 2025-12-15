# py-basketball

Objectives

-   Frontend

    -   Libraries
        -   [React](https://react.dev/learn)
        -   [TypeScript](typescriptlang.org/cheatsheets/)
        -   [@tanstack/tanstack-router](https://tanstack.com/router/latest) - Routing
        -   [@tanstack/query](https://tanstack.com/query/latest) - Data retrieval
        -   [zustand](https://github.com/pmndrs/zustand) - Global state
    -   Features
        -   Users
            -   [ ] Sign up page
            -   [ ] Login page
            -   [ ] Home page
        -   Generic features
            -   [ ] Watching players (tracking trends for specific players)
                -   [ ] Render playerlist
                -   [ ] Call backend service for updating watchlist
            -   [x] List of trending players in the NBA
                -   [x] Filter tag selector
        -   Yahoo API
            -   [ ] Prompt user to connect Yahoo account
            -   [ ] Show current matchup
            -   [ ] Show list of trending players based on league settings
            -   [ ] Dashboard
                -   [ ] Today's games
                -   [ ] Waiver board
                -   [ ] Category tracker

-   Backend
    -   Selenium (Proof of concept, will not be used in production)
        -   [x] Scrape data from [basketball-reference](https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=11&day=17&year=2025) for player stats
        -   [x] Scrape data from [basketball-reference](https://www.basketball-reference.com/allstar/202502162NBA.html) for list of all stars
    -   External Services
        -   [x] Retrieve upcoming NBA schedule for the next N days
        -   [x] Retrieve player stats from NBA API
    -   Supabase
        -   [x] player_data table - Saved player statistics
        -   [x] saved_dates table - Indicates which dates have already been scraped
        -   [x] analysis_status table - Save process status for projected analysis
        -   [x] analysis_data table - Save data for projected analysis
        -   [x] trending_analysis_status table - Save process status for trending analysis
        -   [x] trending_analysis_data table - Save data for trending analysis
        -   [x] Supabase functions for grabbing all/average/totals of player stats from the last N days
    -   [ ] Use AI for player analysis (trends and projections)
        -   [x] Google Gemini
            -   [ ] Determine work around for January 2025 knowledge cut off
                -   [x] Pull list of all stars for recent years
            -   [ ] Feed entire season data set for all players and schedule (Will need to workaround API Limits)
                -   [ ] Use different AI API?
        -   [x] Feed statistics from the last N days
        -   [x] Get projected statistics for the next N days
        -   [x] Get trending players from the past N days
            -   [ ] Add parameters for filters
            -   [ ] Player tags
                -   [ ] Injury
                -   [x] Minutes Up
                -   [x] Stocks
                -   [ ] Usage
        -   [x] Incorporate upcoming NBA schedule
            -   [x] Get number of games for next N days
            -   [x] Get list of opponents for next N days
    -   [ ] Automation
        -   [ ] Automate daily/weekly analysis for N days
        -   [x] Pull data once per day and cache pervious analysis results
            -   [x] Run analysis as background process background
    -   [ ] fastapi routes for:
        -   [ ] Authentication - require Supabase JWT token to access routes
        -   [ ] Accessing player statistics
            -   [x] Projected players for the next N days
            -   [x] Player averages from last N days
            -   [x] ProjectedAnalysis for the next N days
            -   [x] Trending players from last N days
            -   [x] Fantasy score calculation
                -   [x] Create exclusion list based off fantasy scores
        -   [ ] Passing specific criteria for analysis (Dependent on API rate limits (Too much data?))
        -   [ ] Personalized analysis for current user
            -   [ ] Watch list
    -   [ ] Yahoo API
        -   [ ] Link user account to Yahoo fantasy league
            -   [ ] OAuth and Yahoo Developer API
        -   [ ] Exclude highest rostered players from analysis
        -   [ ] Analyze current user matchup

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r src/server/requirements.txt
pip install
npm install --prefix ./src/client
```

Create an .env file in the root directory with the folllowing contents:

```properties
SUPABASE_URL=YOUR_SUPABASE_URL_HERE
SUPABASE_KEY=YOUR_SUPABASE_KEY_HERE
SUPABASE_JWT_SECRET=YOUR_SUPABASE_JWT_SECRET_HERE
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
python3 -m venv .venv
.venv/Scripts/activate

cd src/server
pip install -r requirements.txt
fastapi dev main.py --port 3300
```

## Run Client

```bash
cd src/client
npm run dev
```
