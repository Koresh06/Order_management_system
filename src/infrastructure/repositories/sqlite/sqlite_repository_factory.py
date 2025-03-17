from src.domain.repositories.base_repository import BaseRepository
from src.infrastructure.repositories.base_repository_factory import RepositoryFactory
from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.sqlite.implementation.users_repository_impl import SQLiteUsersRepositoryImpl
from src.infrastructure.repositories.sqlite.implementation.orders_repository_impl import SQLiteOrdersRepositoryImpl
from src.infrastructure.repositories.sqlite.implementation.products_repository_impl import SQLiteProductsRepositoryImpl


class SQLiteRepositoryFactory(RepositoryFactory):
    def create_user_repository(self, db_helper: SQLiteDatabaseHelper) -> BaseRepository:
        return SQLiteUsersRepositoryImpl(db_helper)
    
    def create_product_repository(self, db_helper: SQLiteDatabaseHelper) -> BaseRepository:
        return SQLiteProductsRepositoryImpl(db_helper)

    def create_order_repository(self, db_helper: SQLiteDatabaseHelper) -> BaseRepository:
        return SQLiteOrdersRepositoryImpl(db_helper)
