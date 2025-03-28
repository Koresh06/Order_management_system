from abc import ABC, abstractmethod

from src.domain.entitys.cart_item import CartItemModel


class CartItemServiceInterface(ABC):

    @abstractmethod
    def add_item(self, order_item: CartItemModel) -> CartItemModel:
        ...

    @abstractmethod
    def update_cart_quantity(self, cart_item: CartItemModel, item_id: int, quantity: int) -> CartItemModel:
        ...