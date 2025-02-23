__all__ = [
    "api_router",
]

from core import settings
from fastapi import APIRouter

from api.v1 import router as v1_router

api_router = APIRouter(prefix=settings.api.prefix)

# Include v1 Routers
api_router.include_router(
    v1_router,
)
