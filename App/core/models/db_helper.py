from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str):
        self.engine: AsyncEngine = create_async_engine(url=url)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self):
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(str(settings.db.url))
