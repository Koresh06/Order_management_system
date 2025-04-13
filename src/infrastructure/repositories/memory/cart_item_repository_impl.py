from src.domain.repositories.cart_item_repository_intarface import CartItemRepositoryInterface
from src.domain.entitys.cart_item import CartItemEntryModel, CartItemModel
from src.domain.entitys.item import ItemModel


class CartItemRepositoryImpl(CartItemRepositoryInterface):
    def __init__(self):
        self.cart_items = []
        self.counter = 1

    def create_cart_item(self, new_cart_item: CartItemModel) -> CartItemModel:
        new_cart_item.id = self.counter
        self.cart_items.append(new_cart_item)
        self.counter += 1
        return new_cart_item

    def add(self, cart_item: CartItemModel, cart_entry_item: CartItemEntryModel) -> CartItemModel:
        for cart in self.cart_items:
            cart.total_price = cart_item.total_price
            if cart.user_id == cart_item.user_id:
                cart.items.append(cart_entry_item)    
                return cart

    def get_item_in_cart(self, user_id: int, item_id: int) -> CartItemModel:
        for cart_item in self.cart_items:
            if cart_item.user_id == user_id:
                for element in cart_item.items:
                    if element.item.id == item_id:
                        return cart_item
    
    def get_cart_by_id_user(self, user_id: int) -> CartItemModel:
        for cart_item in self.cart_items:
            if cart_item.user_id == user_id:
                return cart_item

    def update_cart_item(
        self,
        cart_item: CartItemModel,
        item_id: int,
        updated_data: dict,
    ) -> CartItemModel:
        for cart in self.cart_items:
            if cart.id == cart_item.id:
                for element in cart.items:
                    if element.item.id == item_id:
                        for key, value in updated_data.items():
                            setattr(element, key, value)
                        return cart
    
    def delete_by_id_item(self, cart_item: CartItemModel, item_id: int) -> bool:
        for item in self.cart_items:
            if item.id == cart_item.id and item.item_id == item_id:
                self.cart_items.remove(item)
