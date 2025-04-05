from dependency_injector import containers, providers

from src.application.services.cart_item.cart_item_service import CartItemService
from src.infrastructure.repositories.memory.cart_item_repository_impl import CartItemRepositoryImpl
from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl
from src.infrastructure.repositories.memory.item_repository_impl import ItemRepositoryImpl
from src.application.use_cases.use_case_cart_item import AddCartItemUseCase, DeleteItemInCartUseCase, GetAllItemsInUserCartUseCase, UpdateItemInCartUseCase


class CartItemContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    cart_item_repo = providers.Singleton(CartItemRepositoryImpl)
    user_repo = providers.Singleton(UserRepositoryImpl)
    item_repo = providers.Singleton(ItemRepositoryImpl)

    cart_item_service = providers.Singleton(
        CartItemService,
        cart_item_repo=cart_item_repo,
        user_repo=user_repo,
        item_repo=item_repo,
    )

    add_cart_item_use_case = providers.Factory(
        AddCartItemUseCase,
        service=cart_item_service,
    )

    get_all_by_cart_user = providers.Factory(
        GetAllItemsInUserCartUseCase,
        service=cart_item_service,
    )

    update_item_in_cart_use_case = providers.Factory(
        UpdateItemInCartUseCase,
        service=cart_item_service,
    )
    
    delete_item_in_cart_use_case = providers.Factory(
        DeleteItemInCartUseCase,
        service=cart_item_service,
    )