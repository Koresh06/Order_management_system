from abc import ABC, abstractmethod

from src.domain.entitys.user import UserModel   


class UserServiceInterface(ABC):

    @abstractmethod
    def create_user(self, user: UserModel) -> UserModel:
        ...

    @abstractmethod
    def get_all(self) -> list[UserModel]:
        ...

    @abstractmethod
    def delete(self, id: int) -> bool:
        ...