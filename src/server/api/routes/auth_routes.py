"""Routes for creating and authenticating users"""
from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.responses import RedirectResponse, Response
from api.auth import get_current_user
import config
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
        
        return RedirectResponse(url=config.CLIENT_URL)
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
        redirect_response = RedirectResponse(url=config.CLIENT_URL, status_code=status.HTTP_303_SEE_OTHER)
        redirect_response.set_cookie(key='access_token', value=f'Bearer {access_token}', httponly=True)
        return redirect_response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get('/logout')
async def logout(response: Response):
    redirect_response = RedirectResponse(url=config.CLIENT_URL, status_code=status.HTTP_303_SEE_OTHER)
    redirect_response.delete_cookie(key='access_token')
    return redirect_response

@router.get('/validate')
async def validate_current_user(response: Response, current_user = Depends(get_current_user)):
    return True
