from fastapi import APIRouter

from app.api.api_v1.endpoints import batches


api_router = APIRouter()
api_router.include_router(batches.router, prefix="/batches", tags=["batches"])
