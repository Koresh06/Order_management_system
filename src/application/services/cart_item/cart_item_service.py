from src.domain.entitys.cart_item import CartItemModel
from src.domain.repositories.cart_item_repository_intarface import CartItemRepositoryInterface
from src.application.services.cart_item.cart_item_service_intarface import CartItemServiceInterface  


class ExistCartItemException(Exception):
    pass


class CartItemService(CartItemServiceInterface):
    def __init__(
        self, 
        cart_item_repo: CartItemRepositoryInterface,
    ):
        self.cart_item_repo = cart_item_repo

    def add_item(self, cart_item: CartItemModel) -> CartItemModel:
        existing_item = self.cart_item_repo.get_cart_item(cart_item.user_id, cart_item.item_id)

        if existing_item:
            raise ExistCartItemException("Cart item already exists in the cart")

        return self.cart_item_repo.add(cart_item)
    
    def update_cart_quantity(self, cart_item: CartItemModel, item_id: int, quantity: int) -> CartItemModel:
        self.cart_item_repo.update_cart_item(cart_item=cart_item, item_id=item_id, updated_data={"quantity": quantity})
        