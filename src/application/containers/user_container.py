from dependency_injector import containers, providers

from src.application.services.users.user_service import UserService
from src.application.services.users.security import PasswordHasher
from src.application.use_cases.user_use_case import GetAllUsersUseCase, RegisterUserUseCase
from src.infrastructure.external_services.send_email import EmailService
from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl


class UserContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repo = providers.Singleton(UserRepositoryImpl)

    password_hasher = providers.Singleton(PasswordHasher)

    email_service = providers.Singleton(EmailService)

    user_service = providers.Singleton(
        UserService,
        user_repo=user_repo,
        password_hasher=password_hasher,
        email_service=email_service,
    )

    register_user_use_case = providers.Factory(
        RegisterUserUseCase,
        service=user_service,
    )

    get_all_users_use_case = providers.Factory(
        GetAllUsersUseCase,
        service=user_service,
    )
