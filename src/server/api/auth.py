from fastapi import Request, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from config import SUPABASE_JWT_SECRET

security = HTTPBearer()

async def auth_middleware(request: Request, call_next):
    """Middleware to append bearer token to request"""
    token = __strip_bearer(request.cookies.get('access_token'))
    if token:
        request.headers.__dict__['_list'].append(
            [b'authorization', f'Bearer {token}'.encode()]
        )
    response = await call_next(request)
    return response

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Retrieves current user if token is valid"""
    try:
        token = __strip_bearer(credentials.credentials)
        payload = jwt.decode(token, SUPABASE_JWT_SECRET, algorithms=['HS256'], options={ 'verify_aud': False })
        user_id = payload.get('sub')
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has expired')
    except jwt.PyJWKError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Failed to validate user')

def __strip_bearer(bearer_token: str) -> str:
    """Strips 'Bearer' string from token"""
    if bearer_token is not None:
        return bearer_token.replace('Bearer ', '')
    return bearer_token