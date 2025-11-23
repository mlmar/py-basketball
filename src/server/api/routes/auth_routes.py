"""Routes for creating and authenticating users"""
from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import Response
from lib.db.client import get_client

router = APIRouter()

@router.post('/signup')
async def signup(email: str = Form(), password: str = Form()):
    try:
        auth_response = get_client().auth.sign_up({ 
            'email': email, 
            'password': password 
        })
        if auth_response.user is None:
            raise HTTPException(status_code=400, detail="Sign Up Failed")
        
        return auth_response.user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post('/login')
async def login(response: Response, email: str = Form(), password: str = Form()):
    try:
        auth_response = get_client().auth.sign_in_with_password({ 
            'email': email, 
            'password': password 
        })
        if auth_response.user is None:
            raise HTTPException(status_code=400, detail="Login Failed")
        
        access_token = auth_response.session.access_token
        response.set_cookie(key='access_token', value=f'Bearer {access_token}', httponly=True)
        return access_token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get('logout')
async def logout(response: Response):
    response.delete_cookie(key='access_token')
    return response