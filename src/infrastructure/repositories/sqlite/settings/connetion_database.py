from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker


class IDatabase(ABC):
    @abstractmethod
    def get_engine(self) -> AsyncEngine:
        pass

    @abstractmethod
    def get_sessionmaker(self) -> sessionmaker:
        pass

    @abstractmethod
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        pass
