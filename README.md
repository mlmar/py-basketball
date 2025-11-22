# py-basketball

Objectives

- [ ] Frontend
  - [ ] Angular
- [ ] Backend
  - [ ] Selenium
    - [x] Scrape data from [basketball-reference](https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=11&day=17&year=2025)
  - [x] External Services
    - [x] Retrieve upcoming NBA schedule for the next N days
  - [x] Supabase
    - [x] player_data table - Saved player statistics
    - [x] saved_dates table - Indicates which dates have already been scraped
    - [x] Supabase functions for grabbing all/average/totals of player stats from the last N days
  - [ ] Use AI to analyse player data and create projects
    - [x] Google Gemini
      - [ ] Determine work around for January 2025 knowledge cut off
      - [ ] Use different AI API?
      - [ ] Feed entire season data set and schedule (Will have to deal with API Limits)
    - [x] Feed statistics from the last N days
    - [x] Get projected statistics for the next N days
    - [x] Incorporate upcoming NBA schedule
      - [x] Get number of games for next N days
      - [x] Get list of opponents for next N days
  - [ ] Automation
    - [ ] Automate daily/weekly analysis for N days
  - [ ] fastapi routes for:
    - [ ] Serving front end application
    - [ ] Accessing player statistics

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r src/server/requirements.txt
```
