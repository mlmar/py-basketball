from typing import Generator
from datetime import timedelta
from datetime import date

def range_of_dates(start_date: date, end_date: date) -> Generator[date]:
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)