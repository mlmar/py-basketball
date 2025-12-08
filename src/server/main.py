from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.routes import stats_routes, auth_routes
from api.auth import auth_middleware
import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:3000',
        'https://waiverwarrior.vercel.app'
    ],
    allow_credentials=True,  
    allow_methods=['*'],
    allow_headers=['*']
)


# app.middleware('http')(auth_middleware) # Commenting out middleware for now
app.include_router(auth_routes.router)
app.include_router(stats_routes.router)

# Mount static path
if not config.DEV:
    app.mount("/", StaticFiles(directory="static", html=True), name="static")