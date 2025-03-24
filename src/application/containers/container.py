from dependency_injector import containers, providers

from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl
from src.infrastructure.repositories.memory.role_repository_impl import RoleRepositoryImpl

from src.application.services.users.user_service_impl import UserServiceImpl



class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repository = providers.Singleton(UserRepositoryImpl)
    role_repository = providers.Singleton(RoleRepositoryImpl)

    user_service = providers.Factory(
        UserServiceImpl,
        user_repo=user_repository, 
        role_repo=role_repository   
    )

    