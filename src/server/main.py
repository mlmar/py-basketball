from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import stats_routes, auth_routes
from api.auth import auth_middleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:3000',
        'https://waiverwire.vercel.app'
    ],
    allow_credentials=True,  
    allow_methods=['*'],
    allow_headers=['*']
)


# app.middleware('http')(auth_middleware) # Commenting out middleware for now
app.include_router(auth_routes.router)
app.include_router(stats_routes.router)