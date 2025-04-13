from abc import ABC, abstractmethod

from src.domain.entitys.order import OrderModel
from src.domain.entitys.cart_item import CartItemModel


class OrderRepositoryInterface(ABC):
    @abstractmethod
    def create(
        self,
        user_id: int,
        total_price: float,
        items: CartItemModel,
    ) -> OrderModel: ...

    @abstractmethod
    def get_by_id(self, order_id: int) -> OrderModel: ...
