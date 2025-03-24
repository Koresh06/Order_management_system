from datetime import datetime

from src.application.services.users.user_service_interface import UserServiceInterface
from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.repositories.role_repository_intarface import RoleRepositoryInterface
from src.domain.entitys.user import UserModel

from src.application.services.users.exception import NotFoundRole


class UserServiceImpl(UserServiceInterface):
    def __init__(
        self,
        user_repo: UserRepositoryInterface,
        role_repo: RoleRepositoryInterface,
    ):
        self.user_repo = user_repo
        self.role_repo = role_repo

    def create_user(self, user: UserModel) -> UserModel:
        if self.role_repo.get_by_id(user.role_id) is None:
            raise NotFoundRole("Role id not found")
        if self.user_repo.get_by_username(user.username) is not None:
            raise Exception("User already exists")
        return self.user_repo.create(user)


    def get_all(self) -> list[UserModel]:
        return self.user_repo.get_all()