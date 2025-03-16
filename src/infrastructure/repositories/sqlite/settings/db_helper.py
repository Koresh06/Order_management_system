from collections.abc import Generator

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.infrastructure.repositories.sqlite.settings.connetion_database import IDatabase
from src.utils.config import settings


class SQLiteDatabaseHelper(IDatabase):
    def __init__(self):
        self.engine = self.get_engine()
        self.sessionmaker = self.get_sessionmaker()

    def get_engine(self):
        return create_engine(
            url=settings.db.sqlite.url,
            echo=settings.db.sqlite.echo,
        )

    def get_sessionmaker(self):
        return sessionmaker(bind=self.engine, expire_on_commit=False, autoflush=False)

    def get_session(self) -> Generator:
        return self.sessionmaker()
