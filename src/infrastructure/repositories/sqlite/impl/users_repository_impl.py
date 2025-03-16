from sqlalchemy import select
from src.domain.repositories.user_repository import UserRepositoryABC
from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.models.users import User
from src.presentation.api.users.schemas import UserCreateSchema


class UsersRepositorySQLiteImpl(UserRepositoryABC):
    def __init__(self, db_helper: SQLiteDatabaseHelper):
        self.db_helper = db_helper

    def create(self, user: UserCreateSchema) -> User:
        with self.db_helper.get_session() as session:
            create_user = User(
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            session.add(create_user)
            session.commit()
            session.refresh(create_user)
            return create_user

    def get_all(self) -> list[User]:
        with self.db_helper.get_session() as session:
            return session.scalars(select(User)).all()

    def get_by_id(self, id: int) -> User:
        with self.db_helper.get_session() as session:
            return session.get(User, id)

    def update(
        self,
        user: User,
        user_update: dict,
        partial: bool = False,
    ) -> User:
        with self.db_helper.get_session() as session:
            user_from_db = session.get(User, user.id)
            for key, value in user_update.model_dump(exclude_unset=partial).items():
                setattr(user_from_db, key, value)
            session.commit()
            session.refresh(user_from_db)
            return user

    def delete(self, id: int) -> None:
        with self.db_helper.get_session() as session:
            user = session.get(User, id)
            session.delete(user)
            session.commit()
