from fastapi import APIRouter
from datetime import date as _date

from service.nba_cdn_service import get_nba_schedule
from util.date_util import str_to_date

router = APIRouter()

@router.get('/nba-schedule')
def get_schedule(date: str, future_days: int):
    return get_nba_schedule(str_to_date(date), future_days)