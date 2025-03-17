from src.application.services.base_service import BaseService
from src.domain.entitys.user import UserModel
from src.domain.repositories.base_repository import BaseRepository


class UsersServiceImpl(BaseService):
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def create(self, user: UserModel) -> UserModel:
        return self._repository.create(user)

    def get_all(self) -> list[UserModel]:
        return self._repository.get_all()

    def get_by_id(self, id: int) -> UserModel:
        return self._repository.get_by_id(id)

    def update(
        self,
        user: UserModel,
        user_update: UserModel,
        partial: bool = False,
    ) -> UserModel:
        return self._repository.update(
            user=user,
            user_update=user_update,
            partial=partial,
        )

    def delete(self, id: int) -> None:
        return self._repository.delete(id)
