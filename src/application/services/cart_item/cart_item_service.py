from src.domain.entitys.cart_item import CartItemModel
from src.domain.repositories.cart_item_repository_intarface import CartItemRepositoryInterface
from src.application.services.cart_item.cart_item_service_intarface import CartItemServiceInterface


class ExistCartItemException(Exception):
    pass

class NotFoundCartItemException(Exception):
    pass


class CartItemService(CartItemServiceInterface):
    def __init__(
        self,
        cart_item_repo: CartItemRepositoryInterface,
    ):
        self.cart_item_repo = cart_item_repo



    def exist_cart_item(self, user_id: int, item_id: int) -> bool:
        existing_item = self.cart_item_repo.get_cart_item(user_id, item_id)

        if existing_item:
            raise ExistCartItemException("Cart item already exists in the cart")

    def add_item(self, cart_item: CartItemModel) -> CartItemModel:
        self.exist_cart_item(cart_item.user_id, cart_item.item_id)
        return self.cart_item_repo.add(cart_item)

    def get_all(self) -> list[CartItemModel]:
        return self.cart_item_repo.get_all()

    def get_by_cart(self, cart_id: int) -> CartItemModel:
        cart = self.cart_item_repo.get_by_cart(cart_id)
        if not cart:
            raise NotFoundCartItemException("Cart not found")
        return cart

    def update_cart_quantity(
        self,
        cart_item: CartItemModel,
        item_id: int,
        quantity: dict,
    ) -> CartItemModel:
        return self.cart_item_repo.update_cart_item(
            cart_item=cart_item,
            item_id=item_id,
            updated_data={"quantity": quantity},
        )

    def delete_cart_item(self, cart_item: CartItemModel, item_id: int) -> None:
        self.cart_item_repo.delete_by_id_item(cart_item=cart_item, item_id=item_id)