

from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

from api.auth import get_current_user, get_redirect_response
import config
from lib.db.database_table import get_table
from lib.yahoo import yahoo_auth

router = APIRouter(prefix='/yahoo')

@router.get('/login')
def login(current_user = Depends(get_current_user)) -> RedirectResponse:
    """Logs into yahoo account, inserts user id to tokens table, and redirects to yahoo url"""
    user_id = current_user['id']
    state = f'{user_id},{current_user['token']}'
    auth_url = yahoo_auth.build_authorization_url(redirect_uri=config.YAHOO_REDIRECT_URL, state=state)
    tokens_table = get_table(config.SUPABASE_TOKENS_TABLE, config.SUPABASE_SCHEMA)
    tokens_table.upsert({
        'uid': user_id
    }).execute()
    return RedirectResponse(url=auth_url)

@router.get('/authenticate')
def authenticate(code: str = None, state: str = None) -> RedirectResponse:
    """Exchanges yahoo code for tokens, updates refresh token in tokebs table, then redirects to client"""
    tokens = yahoo_auth.exchange_code_for_token(code)
    
    [uid, access_token] = state.split(',')

    tokens_table = get_table(config.SUPABASE_TOKENS_TABLE, config.SUPABASE_SCHEMA)
    tokens_table.update({
        'refresh_token': tokens['refresh_token'],
        'expires_in': tokens['expires_in']
    }).eq('uid', uid).execute()

    return get_redirect_response(access_token=access_token, yahoo_token=tokens['access_token'])

@router.get('/validate')
def validate(request: Request, current_user = Depends(get_current_user)):
    yahoo_token = request.cookies.get('yahoo_token')
    if yahoo_token:
        return True
    return False