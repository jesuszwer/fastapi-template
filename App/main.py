from core.config import settings
from fastapi import FastAPI

main_app = FastAPI()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:main_app",
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.reload,
    )
