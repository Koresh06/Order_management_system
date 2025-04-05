from abc import ABC, abstractmethod

from src.domain.entitys.user import UserModel


class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def create(self, user: UserModel) -> UserModel:
        ...


    @abstractmethod
    def get_all(self, limit: int, offset: int) -> list[UserModel]:
        ...


    @abstractmethod
    def get_by_username(self, username: str) -> UserModel:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> UserModel:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> UserModel:
        ...

    @abstractmethod
    def delete(self, id: int) -> None:
        ...