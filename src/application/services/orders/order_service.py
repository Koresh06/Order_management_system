from src.application.services.orders.exceptions import CartItemNotFoundError, OrderNotFoundError
from src.domain.entitys.order import OrderModel
from src.domain.repositories.cart_item_repository_intarface import CartItemRepositoryInterface
from src.domain.repositories.order_repository_intarface import OrderRepositoryInterface
from src.domain.services.order.order_service_intarface import OrderServiceInterface


class OrderService(OrderServiceInterface):
    def __init__(
        self,
        order_repo: OrderRepositoryInterface,
        cart_item_repo: CartItemRepositoryInterface,
    ) -> None:
        self.order_repo = order_repo
        self.cart_item_repo = cart_item_repo

    def create(self, user_id: int) -> OrderModel:
        if self.cart_item_repo.get_cart_by_id_user(user_id) is None:
            raise CartItemNotFoundError("Cart is empty")
        
        cart_items = self.cart_item_repo.get_cart_by_id_user(user_id)

        order = self.order_repo.create(
            user_id=user_id,
            items=cart_items,
            total_price=cart_items.total_price,
        )
        self.cart_item_repo.cancel_cart(user_id)

        return order

    def get_by_id(self, order_id: int) -> OrderModel:
        if self.order_repo.get_by_id(order_id) is None:
            raise OrderNotFoundError("Order not found")
        
        return self.order_repo.get_by_id(order_id)
    

    def get_all_orders_by_user(self, user_id: int) -> list[OrderModel]:
        return self.order_repo.get_all_orders_by_user(user_id)
    

    def get_all_orders(self) -> list[OrderModel]:
        return self.order_repo.get_all()
    
    
    def delete(self, order_id: int) -> None:
        return self.order_repo.delete(order_id)
