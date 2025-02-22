from contextlib import asynccontextmanager

from core import db_helper
from core.config import settings
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup

    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:main_app",
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.reload,
    )
