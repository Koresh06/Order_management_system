from datetime import datetime
from src.domain.repositories.base_repository import BaseRepository
from src.domain.entitys.user import UserModel


class MemoryUsersRepositoryImpl(BaseRepository):
    def __init__(self):
        self.users = []
        self.counter = 0

    def create(self, user: UserModel) -> UserModel:
        self.counter += 1
        new_user = UserModel(
            id=self.counter,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.users.append(new_user)
        return new_user

    def get_all(self) -> list[UserModel]:
        return self.users

    def get_by_id(self, id: int) -> UserModel:
        for user in self.users:
            if user.id == id:
                return user
        return None

    def update(
        self,
        user: UserModel,
        user_update: UserModel,
        partial: bool = False,
    ) -> UserModel:
        for index, item in enumerate(self.users):
            if item.id == user.id:
                for key, value in user_update.model_dump(exclude_unset=partial).items():
                    setattr(item, key, value)
                self.users[index] = item
                return item
        return None

    def delete(self, id: int) -> None:
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                return None
