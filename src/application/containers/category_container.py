from dependency_injector import containers, providers

from src.application.services.categories.category_service import CategoryService
from src.infrastructure.repositories.memory.category_repository_impl import CategoryRepositoryImpl
from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl
from src.application.use_cases.category_use_case import CreateCategoryUseCase


class CategoryContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    category_repo = providers.Singleton(CategoryRepositoryImpl)
    user_repo = providers.Singleton(UserRepositoryImpl)
    
    category_service = providers.Singleton(
        CategoryService,
        category_repo=category_repo,
        user_repo=user_repo,
    )

    create_category_use_case = providers.Factory(
        CreateCategoryUseCase,
        service=category_service,
    )
