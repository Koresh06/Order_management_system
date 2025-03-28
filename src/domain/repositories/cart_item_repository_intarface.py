from abc import ABC, abstractmethod

from src.domain.entitys.cart_item import CartItemModel


class CartItemRepositoryInterface(ABC):

    @abstractmethod
    def add(self, cart_item: CartItemModel) -> CartItemModel:
        ...

    @abstractmethod
    def get_cart_item(self, user_id: int, item_id: int) -> CartItemModel:
        ...

    @abstractmethod
    def update_cart_item(self, cart_item: CartItemModel, item_id: int, updated_data: dict) -> CartItemModel:
        ...