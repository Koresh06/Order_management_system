from abc import ABC, abstractmethod

from src.domain.entitys.cart_item import CartItemModel


class CartItemServiceInterface(ABC):

    @abstractmethod
    def add_item(self, cart_item: CartItemModel, item_id: int, quantity: int) -> CartItemModel: ...

    @abstractmethod
    def get_by_cart(self, cart_id: int) -> CartItemModel: ...

    @abstractmethod
    def get_items_by_user(self, user_id: int) -> list[CartItemModel]: ...

    @abstractmethod
    def update_cart_quantity(
        self,
        cart_item: CartItemModel,
        item_id: int,
        quantity: int,
    ) -> CartItemModel: ...

    @abstractmethod
    def delete_item_in_cart(self, cart_item: CartItemModel, item_id: int) -> bool: ...