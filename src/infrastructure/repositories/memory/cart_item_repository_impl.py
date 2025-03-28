from src.domain.repositories.cart_item_repository_intarface import CartItemRepositoryInterface
from src.domain.entitys.cart_item import CartItemModel


class CartItemRepositoryImpl(CartItemRepositoryInterface):
    def __init__(self):
        self.cart_items = []
        self.counter = 1

    def add(self, cart_item: CartItemModel) -> CartItemModel:
        new_cart_item = CartItemModel(
            id=self.counter,
            user_id=cart_item.user_id,
            item_id=cart_item.item_id,
            quantity=cart_item.quantity,
        )
        self.cart_items.append(new_cart_item)
        self.counter += 1
        return new_cart_item
    
    def get_cart_item(self, user_id: int, item_id: int) -> CartItemModel:
        for cart_item in self.cart_items:
            if cart_item.user_id == user_id and cart_item.item_id == item_id:
                return cart_item
        return None
    
    def update_cart_item(self, cart_item: CartItemModel, updated_data: dict) -> CartItemModel:
        for item in self.cart_items:
            if item.id == cart_item.id:
                for key, value in updated_data.items():
                    setattr(item, key, value)
                return item 
        return None