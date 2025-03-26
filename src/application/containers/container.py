from dependency_injector import containers, providers

from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl
from src.infrastructure.repositories.memory.role_repository_impl import RoleRepositoryImpl
from src.infrastructure.repositories.memory.item_repository_impl import ItemRepositoryImpl
from src.infrastructure.repositories.memory.category_repository_impl import CategoryRepositoryImpl

from src.application.services.users.user_service_impl import UserServiceImpl
from src.application.services.items.item_service_impl import ItemServiceImpl
from src.application.services.categories.category_service_impl import CategoryServiceImpl



class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repository = providers.Singleton(UserRepositoryImpl)
    role_repository = providers.Singleton(RoleRepositoryImpl)
    item_repository = providers.Singleton(ItemRepositoryImpl)
    category_repository = providers.Singleton(CategoryRepositoryImpl)

    user_service = providers.Factory(
        UserServiceImpl,
        user_repo=user_repository, 
        role_repo=role_repository   
    )

    item_service = providers.Factory(
        ItemServiceImpl,
        item_repo=item_repository,
        user_repo=user_repository
    )
    
    category_service = providers.Factory(
        CategoryServiceImpl,
        category_repo=category_repository,
        user_repo=user_repository,
    )