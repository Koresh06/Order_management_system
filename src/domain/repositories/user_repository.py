from abc import ABC, abstractmethod

from src.domain.entitys.user import User


class UserRepositoryABC(ABC):
    @abstractmethod
    def create(self, user) -> User:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def update(self, user) -> User:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
