from abc import ABC, abstractmethod

from src.domain.entitys.cart_item import CartItemModel


class CartItemRepositoryInterface(ABC):

    @abstractmethod
    def add(self, cart_item: CartItemModel) -> CartItemModel: ...

    @abstractmethod
    def get_by_cart(self, cart_id: int) -> CartItemModel: ...

    @abstractmethod
    def get_item_in_cart(self, user_id: int, item_id: int) -> CartItemModel: ...

    @abstractmethod
    def get_items_cart_user(self, user_id: int) -> list[CartItemModel]: ...

    @abstractmethod
    def get_by_id(self, cart_id: int) -> CartItemModel: ...

    @abstractmethod
    def update_cart_item(
        self,
        cart_item: CartItemModel,
        item_id: int,
        updated_data: dict,
    ) -> CartItemModel: ...

    @abstractmethod
    def delete_by_id_item(self, cart_item: CartItemModel, item_id: int) -> None: ...