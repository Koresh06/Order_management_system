from src.application.services.base_service import BaseService
from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.entitys.user import UserModel


class UsersUseCaseImpl(BaseUseCase):
    def __init__(self, service: BaseService):
        self._service = service

    def create(self, user: UserModel) -> UserModel:
        return self._service.create(user)

    def get_all(self) -> list[UserModel]:
        return self._service.get_all()

    def get_by_id(self, id: int) -> UserModel:
        return self._service.get_by_id(id)

    def update(
        self,
        user: UserModel,
        user_update: UserModel,
        partial: bool = False,
    ) -> UserModel:
        return self._service.update(
            user=user,
            user_update=user_update,
            partial=partial,
        )

    def delete(self, id: int) -> None:
        return self._service.delete(id)
