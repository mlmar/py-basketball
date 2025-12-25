

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from api.auth import get_current_user
import config
from lib.yahoo import yahoo_auth

router = APIRouter(prefix='/yahoo')

@router.get('/login')
def login(credentials = Depends(get_current_user)):
    auth_url = yahoo_auth.build_authorization_url(redirect_uri=config.YAHOO_REDIRECT_URL)
    return RedirectResponse(url=auth_url)

@router.get('/authenticate')
def authenticate(code: str = None, state: str = None):
    return { 'code': code, 'state': state }