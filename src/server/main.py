from fastapi import FastAPI
from api.routes import stats_routes, auth_routes
from api.auth import auth_middleware

app = FastAPI()
app.middleware('http')(auth_middleware)
app.include_router(auth_routes.router)
app.include_router(stats_routes.router)