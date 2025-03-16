from abc import ABC, abstractmethod
from src.domain.entitys.user import UserModel


class UsersUseCaseABC(ABC):
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
    def update(self, user_update: dict) -> UserModel:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
