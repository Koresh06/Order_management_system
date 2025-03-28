from datetime import datetime
from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.entitys.user import UserModel
from src.domain.entitys.role import RoleModel

from src.application.services.users.security import _hash_password


class UserRepositoryImpl(UserRepositoryInterface):
    def __init__(self):
        self.users = [
            UserModel(
                id=1,
                username="admin",
                role_id=1,
                email="admin@localhost",
                full_name="Admin",
                password=_hash_password("admin"),
            ),
            UserModel(
                id=2,
                username="user",
                role_id=2,
                email="user@localhost",
                full_name="User",
                password=_hash_password("user"),
            ),
        ]
        self.counter = 1

    def create(self, user: UserModel) -> UserModel:
        hashed_password = _hash_password(user.password)

        new_user = UserModel(
                id=self.counter,
                username=user.username,
                role_id=user.role_id,
                email=user.email,
                full_name=user.full_name,
                password=hashed_password,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
        self.users.append(new_user)
        self.counter += 1
        return new_user

    def get_all(self) -> list[UserModel]:
        return self.users


    def get_by_username(self, username: str) -> UserModel:
        for user in self.users:
            if user.username == username:
                return user

        return None
    
    def get_by_id(self, id: int) -> UserModel:
        for user in self.users:
            if user.id == id:
                return user

        return None
    
    def delete(self, id: int) -> None:
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                return

        raise Exception("User not found")