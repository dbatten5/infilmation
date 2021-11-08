"""Entrypoint to API routers."""
from fastapi import APIRouter

from app.api import movies
from app.api import utils

api_router = APIRouter()

api_router.include_router(utils.router, tags=["utils"])
api_router.include_router(movies.router, tags=["movies"])
