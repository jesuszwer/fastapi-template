"""
The routes of the API version 1.

This API version has a single health check endpoint.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/v1")


@router.get("/healthcheck")
async def health_check():
    return {"status": "ok"}
