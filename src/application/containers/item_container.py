from dependency_injector import containers, providers

from src.application.services.items.item_service import ItemService
from src.application.services.items.save_file import LocalSaveFileService
from src.infrastructure.repositories.memory.item_repository_impl import ItemRepositoryImpl
from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl
from src.infrastructure.repositories.memory.category_repository_impl import CategoryRepositoryImpl
from src.application.use_cases.item_use_case import CreateItemUseCase, GetAllItemsUseCase, GetAllItemsByUserUseCase


class ItemContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    item_repo = providers.Singleton(ItemRepositoryImpl)
    user_repo = providers.Singleton(UserRepositoryImpl)
    category_repo = providers.Singleton(CategoryRepositoryImpl)

    file_service = providers.Singleton(LocalSaveFileService)

    item_service = providers.Singleton(
        ItemService,
        item_repo=item_repo,
        user_repo=user_repo,
        category_repo=category_repo,
        file_service=file_service,
    )

    create_item_use_case = providers.Factory(
        CreateItemUseCase,
        service=item_service,
    )
    get_all_items_use_case = providers.Factory(
        GetAllItemsUseCase,
        service=item_service,

    )
    get_all_items_by_user_use_case = providers.Factory(
        GetAllItemsByUserUseCase,
        service=item_service,
    )
