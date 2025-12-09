from typing import Generator
from datetime import date, timedelta, timezone, datetime

def range_of_dates(start_date: date, end_date: date) -> Generator[date, None, None]:
    if start_date > end_date: # Switch dates
        temp_date = start_date
        start_date = end_date
        end_date = temp_date

    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def calc_date(start_date: date, num_days: int) -> date:
    return start_date + timedelta(num_days)

def get_today_pst() -> date:
    """Returns date in pacific time zone"""

    # Define a time zone with a UTC offset of -8 hours
    tzinfo = timezone(timedelta(hours=-8))

    # Create an aware datetime object with the specified time zone
    today = date.today()
    aware_datetime = datetime(today.year, today.month, today.day, tzinfo=tzinfo)
    return date(aware_datetime.year, aware_datetime.month, aware_datetime.day)