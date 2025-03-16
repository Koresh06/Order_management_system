from src.domain.repositories.base_repository import BaseRepository
from src.infrastructure.repositories.base_repository_factory import RepositoryFactory
from src.infrastructure.repositories.memory.implementation.orders_repository_impl import MemoryOrdersRepositoryImpl
from src.infrastructure.repositories.memory.implementation.users_repository_impl import MemoryUsersRepositoryImpl


class MemoryRepositoryFactory(RepositoryFactory):
    def create_user_repository(self) -> BaseRepository:
        return MemoryUsersRepositoryImpl()

    def create_order_repository(self) -> BaseRepository:
        return MemoryOrdersRepositoryImpl()
