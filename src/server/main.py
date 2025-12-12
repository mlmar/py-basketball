from pathlib import Path
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api.routes import stats_routes, auth_routes
from api.auth import auth_middleware
import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:3000',
        config.CLIENT_URL
    ],
    allow_credentials=True,  
    allow_methods=['*'],
    allow_headers=['*']
)


app.middleware('http')(auth_middleware) # Commenting out middleware for now
app.include_router(auth_routes.router, prefix='/api')
app.include_router(stats_routes.router, prefix='/api')

# Override routes for static files if production
if not config.DEV:
    frontend_path = Path(__file__).parent / 'static'
    app.mount('/static', StaticFiles(directory=frontend_path, html=True), name='static')

    # Serve index.html for all other non-API routes
    @app.get('/{full_path:path}')
    async def serve_frontend(full_path: str):
        index_html = FileResponse(frontend_path / 'index.html')
        if full_path or full_path.startswith('api'):
            # If static file exists then return it, otherwise return index
            if (frontend_path / full_path).exists():
                return FileResponse(frontend_path / full_path)
            else:
                return index_html
        return index_html
