from dependency_injector import containers, providers

from src.application.services.categories.category_service import CategoryService
from src.domain.repositories.category_repository_intarface import CategoryRepositoryInterface
from src.infrastructure.repositories.memory.category_repository_impl import CategoryRepositoryImpl
from src.application.use_cases.use_case_category import CreateCategoryUseCase


class CategoryContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    category_repo = providers.Singleton(CategoryRepositoryImpl)
    category_service = providers.Singleton(CategoryService, category_repo=category_repo)

    create_category_use_case = providers.Factory(CreateCategoryUseCase, service=category_service)

    