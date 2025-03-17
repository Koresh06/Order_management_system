from dependency_injector import containers, providers

from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.sqlite.sqlite_repository_factory import SQLiteRepositoryFactory
from src.infrastructure.repositories.memory.memory_repository_factory import MemoryRepositoryFactory
from src.application.services.orders_service import OrdersServiceImpl
from src.application.use_cases.orders_user_case import OrdersUseCaseImpl
from src.application.services.users_service import UsersServiceImpl
from src.application.use_cases.users_use_case import UsersUseCaseImpl
from src.application.services.products_service import ProductsServiceImpl
from src.application.use_cases.products_use_case import ProductsUseCaseImpl


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_helper = providers.Singleton(SQLiteDatabaseHelper)

    sqlite_repository_factory = providers.Singleton(SQLiteRepositoryFactory)
    memory_repository_factory = providers.Singleton(MemoryRepositoryFactory)


    users_repository = providers.Singleton(
        sqlite_repository_factory().create_user_repository,
        db_helper=db_helper
    )
    products_repository = providers.Singleton(
        sqlite_repository_factory().create_product_repository,
        db_helper=db_helper
    )
    orders_repository = providers.Singleton(
        sqlite_repository_factory().create_order_repository,
        db_helper=db_helper
    )


    users_service = providers.Factory(
        UsersServiceImpl,
        repository=users_repository
    )
    products_service = providers.Factory(
        ProductsServiceImpl,
        repository=products_repository
    )
    orders_service = providers.Factory(
        OrdersServiceImpl,
        repository=orders_repository
    )


    users_use_case = providers.Factory(UsersUseCaseImpl, service=users_service)
    products_use_case = providers.Factory(ProductsUseCaseImpl, service=products_service)
    orders_use_case = providers.Factory(OrdersUseCaseImpl, service=orders_service)