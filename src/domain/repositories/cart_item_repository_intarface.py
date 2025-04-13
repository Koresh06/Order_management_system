from abc import ABC, abstractmethod

from src.domain.entitys.cart_item import CartItemEntryModel, CartItemModel
from src.domain.entitys.item import ItemModel


class CartItemRepositoryInterface(ABC):

    @abstractmethod
    def create_cart_item(self, new_cart_item: CartItemModel) -> CartItemModel: ...

    @abstractmethod
    def add(self, cart_item: CartItemModel, cart_entry_item: CartItemEntryModel) -> CartItemModel: ...

    @abstractmethod
    def get_item_in_cart(self, user_id: int, item_id: int) -> CartItemModel: ...

    @abstractmethod
    def get_cart_by_id_user(self, user_id: int) -> CartItemModel: ...

    @abstractmethod
    def update_cart_item(
        self,
        cart_item: CartItemModel,
        item_id: int,
        updated_data: dict,
    ) -> CartItemModel: ...

    @abstractmethod
    def delete_by_id_item(self, cart_item: CartItemModel, item_id: int) -> None: ...


    @abstractmethod
    def cancel_cart(self, user_id: int) -> None: ...