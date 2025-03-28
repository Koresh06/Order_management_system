from abc import ABC, abstractmethod

from src.domain.entitys.cart_item import CartItemModel


class CartItemServiceInterface(ABC):

    @abstractmethod
    def add_item(self, cart_item: CartItemModel) -> CartItemModel: ...

    @abstractmethod
    def get_all(self) -> list[CartItemModel]: ...

    @abstractmethod
    def get_by_cart(self, cart_id: int) -> CartItemModel: ...

    @abstractmethod
    def update_cart_quantity(
        self,
        cart_item: CartItemModel,
        item_id: int,
        updated_data: CartItemModel,
    ) -> CartItemModel: ...

    @abstractmethod
    def delete_cart_item(self, cart_item: CartItemModel, item_id: int) -> bool: ...