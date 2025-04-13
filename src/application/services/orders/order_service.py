from src.domain.entitys.order import OrderModel
from src.domain.repositories.cart_item_repository_intarface import CartItemRepositoryInterface
from src.domain.repositories.order_repository_intarface import OrderRepositoryInterface
from src.domain.services.order.order_service_intarface import OrderServiceInterface
from src.domain.services.cart_item.cart_item_service_intarface import CartItemServiceInterface
from src.domain.services.item.item_service_interface import ItemServiceInterface


class OrderService(OrderServiceInterface):
    def __init__(
        self,
        order_repo: OrderRepositoryInterface,
        cart_item_repo: CartItemRepositoryInterface,
    ) -> None:
        self.order_repo = order_repo
        self.cart_item_repo = cart_item_repo

    def create(self, user_id: int) -> OrderModel:
        cart_items = self.cart_item_repo.get_cart_by_id_user(user_id)

        return self.order_repo.create(
            user_id=user_id,
            items=cart_items,
            total_price=cart_items.total_price,
        )

    def get_by_id(self, order_id: int) -> OrderModel:
        return self.order_repo.get_by_id(order_id)
