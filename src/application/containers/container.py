from dependency_injector import containers, providers

from src.application.services.orders_service import OrdersServiceImpl
from src.application.use_cases.order_user_case import OrdersUseCaseImpl
from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.sqlite.sqlite_repository_factory import SQLiteRepositoryFactory
from src.infrastructure.repositories.memory.memory_repository_factory import MemoryRepositoryFactory
from src.application.services.users_service import UsersServiceImpl
from src.application.use_cases.users_use_case import UsersUseCaseImpl


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_helper = providers.Singleton(SQLiteDatabaseHelper)

    sqlite_repository_factory = providers.Singleton(SQLiteRepositoryFactory)
    memory_repository_factory = providers.Singleton(MemoryRepositoryFactory)


    user_repository = providers.Singleton(
        sqlite_repository_factory().create_user_repository,
        db_helper=db_helper
    )
    order_repository = providers.Singleton(
        sqlite_repository_factory().create_order_repository,
        db_helper=db_helper
    )


    users_service = providers.Factory(
        UsersServiceImpl,
        repository=user_repository
    )
    order_service = providers.Factory(
        OrdersServiceImpl,
        repository=order_repository
    )


    users_use_case = providers.Factory(UsersUseCaseImpl, service=users_service)
    order_use_case = providers.Factory(OrdersUseCaseImpl, service=order_service)
