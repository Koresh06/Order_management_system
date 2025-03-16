from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.infrastructure.repositories.sqlite.settings.connetion_database import IDatabase
from src.utils.config import settings


class SQLiteDatabaseHelper(IDatabase):
    def __init__(self):
        self.engine = self.get_engine()
        self.sessionmaker = self.get_sessionmaker()

    def get_engine(self):
        return create_async_engine(
            url=settings.db.sqlite.url,
            echo=settings.db.sqlite.echo,
        )

    def get_sessionmaker(self) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=self.engine, expire_on_commit=False, autoflush=False)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.sessionmaker() as session:
            yield session

        await self.engine.dispose()
