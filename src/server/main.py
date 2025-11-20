from datetime import date, timedelta
from lib.basketball_reference import get_data, PlayerData

end_date = date.today()
start_date = end_date - timedelta(3)

for players in get_data(start_date, end_date):
    print(len(players))
    print()