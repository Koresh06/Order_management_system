from src.application.services.intarface.users_service import UsersServiceABC
from src.domain.entitys.user import UserModel
from src.domain.repositories.user_repository import UserRepositoryABC
from src.presentation.api.users.schemas import UserOutSchema


class UsersServiceImpl(UsersServiceABC):
    def __init__(self, users_repository: UserRepositoryABC):
        self._users_repository = users_repository

    def create(self, user: UserModel) -> UserOutSchema:
        return self._users_repository.create(user)

    def get_all(self) -> list[UserModel]:
        return self._users_repository.get_all()

    def get_by_id(self, id: int) -> UserModel:
        return self._users_repository.get_by_id(id)

    def update(self, user_update: dict) -> UserModel:
        return self._users_repository.update(user_update)

    def delete(self, id: int) -> None:
        return self._users_repository.delete(id)
