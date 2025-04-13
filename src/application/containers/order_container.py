from dependency_injector import containers, providers

from src.application.services.items.save_file import LocalSaveFileService
from src.application.services.orders.order_service import OrderService
from src.domain.entitys.order import OrderModel
from src.application.use_cases.order_use_case import CreateOrderUseCase
from src.application.services.cart_item.cart_item_service import CartItemService
from src.application.services.items.item_service import ItemService
from src.infrastructure.repositories.memory.cart_item_repository_impl import CartItemRepositoryImpl
from src.infrastructure.repositories.memory.category_repository_impl import CategoryRepositoryImpl
from src.infrastructure.repositories.memory.item_repository_impl import ItemRepositoryImpl
from src.infrastructure.repositories.memory.order_repository_impl import OrderRepositoryImpl
from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl

from src.application.containers.cart_item_container import CartItemContainer


class OrderContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    order_repo = providers.Singleton(OrderRepositoryImpl)

    cart_item_service = providers.Dependency()

    order_service = providers.Singleton(
        OrderService,
        order_repo=order_repo,
        cart_item_service=cart_item_service,
    )

    create_order_use_case = providers.Factory(
        CreateOrderUseCase,
        order_service=order_service,
    )

