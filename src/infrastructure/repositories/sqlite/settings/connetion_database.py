from abc import ABC, abstractmethod
from collections.abc import Generator

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker


class IDatabase(ABC):
    @abstractmethod
    def get_engine(self) -> Engine:
        pass

    @abstractmethod
    def get_sessionmaker(self) -> sessionmaker:
        pass

    @abstractmethod
    def get_session(self) -> Generator:
        pass
