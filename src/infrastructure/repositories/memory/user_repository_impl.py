from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.entitys.user import UserModel


DATA_USERS = [
            UserModel(
                id=1,
                username="admin",
                email="admin@localhost.com",
                full_name="Admin",
                password="admin12345",
            ),
            UserModel(
                id=2,
                username="user",
                email="user@localhost.com",
                full_name="User",
                password="user12345",
            ),
        ]

class UserRepositoryImpl(UserRepositoryInterface):
    def __init__(self):
        self.users = DATA_USERS
        self.counter = 1

    def create(self, user: UserModel) -> UserModel:
        new_user = UserModel(
                id=self.counter,
                username=user.username,
                email=user.email,
                full_name=user.full_name,
                password=user.password,
            )
        self.users.append(new_user)
        self.counter += 1
        return new_user

    def get_all(self, limit: int, offset: int) -> list[UserModel]:
        return self.users[offset:offset + limit]


    def get_by_username(self, username: str) -> UserModel:
        for user in self.users:
            if user.username == username:
                return user

        return None
    
    def get_by_email(self, email: str) -> UserModel:
        for user in self.users:
            if user.email == email:
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