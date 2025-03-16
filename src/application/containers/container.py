from dependency_injector import containers, providers

from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.sqlite.impl.users_repository_impl import UsersRepositorySQLiteImpl
from src.application.services.users_service import UsersServiceImpl
from src.application.use_cases.users.use_case import UsersUseCaseImpl


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    dp_halper = providers.Singleton(SQLiteDatabaseHelper)

    users_repository_sqlite = providers.Singleton(
        UsersRepositorySQLiteImpl,
        db_helper=dp_halper,
    )

    users_service = providers.Factory(UsersServiceImpl, users_repository=users_repository_sqlite)

    users_use_case = providers.Factory(UsersUseCaseImpl, users_service=users_service)
