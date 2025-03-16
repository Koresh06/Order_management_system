from abc import ABC, abstractmethod

from src.domain.entitys.user import UserModel


class UserRepositoryABC(ABC):
    @abstractmethod
    def create(self, user: UserModel) -> UserModel:
        pass

    @abstractmethod
    def get_all(self) -> list[UserModel]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> UserModel:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserModel:
        pass

    @abstractmethod
    def update(self, user) -> UserModel:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
