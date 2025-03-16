from src.application.services.users_service import UsersServiceABC
from src.application.use_cases.intarfase.users_use_case import UsersUseCaseABC
from src.domain.entitys.user import UserModel


class UsersUseCaseImpl(UsersUseCaseABC):
    def __init__(self, users_service: UsersServiceABC):
        self._users_service = users_service

    def create(self, user: UserModel) -> UserModel:
        return self._users_service.create(user)

    def get_all(self) -> list[UserModel]:
        return self._users_service.get_all()

    def get_by_id(self, id: int) -> UserModel:
        return self._users_service.get_by_id(id)

    def update(self, user_update: dict) -> UserModel:
        return self._users_service.update(user_update)

    def delete(self, id: int) -> None:
        return self._users_service.delete(id)
