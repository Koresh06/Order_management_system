from sqlalchemy import select
from src.domain.repositories.user_repository import UserRepositoryABC
from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.models.users import User


class UsersRepositorySQLiteImpl(UserRepositoryABC):
    def __init__(self, session: SQLiteDatabaseHelper):
        self.session = session

    async def create(self, user: User) -> User:
        async with self.session.get_session() as session:
            session.add(user)
            await session.commit()
            return user

    async def get_all(self) -> list[User]:
        async with self.session.get_session() as session:
            return await session.scalars(select(User)).all()

    async def get_by_id(self, id: int) -> User:
        async with self.session.get_session() as session:
            return await session.get(User, id)

    async def update(self, user: User, user_update: dict) -> User:
        async with self.session.get_session() as session:
            for key, value in user_update.items():
                setattr(user, key, value)
            await session.commit()
            return user

    async def delete(self, id: int) -> None:
        async with self.session.get_session() as session:
            user = await session.get(User, id)
            await session.delete(user)
            await session.commit()
