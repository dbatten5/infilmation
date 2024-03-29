"""Main app initialization."""
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.api import api_router
from app.core.config import settings
from app.db import database

app = FastAPI(
    title=settings.project_name,
    openapi_url=f"{settings.api_path}/openapi.json",
    docs_url=f"{settings.api_path}/docs/",
    redoc_url=None,
)

app.state.database = database

# Set all CORS enabled origins
if settings.backend_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.backend_cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.api_path)

# simplify operation IDs so that generated API clients have simpler function names
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name


@app.on_event("startup")
async def startup() -> None:
    """Run actions on app startup.

    Ensure database is connected if `persist_film_data` is `True`
    """
    if settings.persist_film_data:
        database_ = app.state.database
        if not database_.is_connected:
            await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Run actions on app shutdown.

    Ensure database is disconnected if `persist_film_data` is `True`
    """
    if settings.persist_film_data:
        database_ = app.state.database
        if database_.is_connected:
            await database_.disconnect()
