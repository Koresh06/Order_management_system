from src.application.services.cart_item.exceptions import CartItemAlreadyExistsError, ItemNotFoundError
from src.application.services.items.exceptions import UserNotFoundError
from src.domain.entitys.cart_item import CartItemModel
from src.domain.repositories.cart_item_repository_intarface import CartItemRepositoryInterface
from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.repositories.item_repository_intarface import ItemRepositoryInterface
from src.domain.services.cart_item.cart_item_service_intarface import CartItemServiceInterface


class CartItemService(CartItemServiceInterface):
    def __init__(
        self,
        cart_item_repo: CartItemRepositoryInterface,
        user_repo: UserRepositoryInterface,
        item_repo: ItemRepositoryInterface,
    ):
        self.cart_item_repo = cart_item_repo
        self.user_repo = user_repo
        self.item_repo = item_repo

    def add_item(self, cart_item: CartItemModel) -> CartItemModel:
        if self.user_repo.get_by_id(cart_item.user_id) is None:
            raise UserNotFoundError(f"User with ID ({cart_item.user_id}) does not exist")

        if self.item_repo.get_by_id(cart_item.item_id) is None:
            raise ItemNotFoundError(f"Item with ID ({cart_item.item_id}) does not exist")

        if self.cart_item_repo.get_item_in_cart(cart_item.user_id, cart_item.item_id) is not None:
            raise CartItemAlreadyExistsError("Cart item already exists in the cart")

        return self.cart_item_repo.add(cart_item)
    
    def get_by_cart(self, cart_id: int) -> CartItemModel:
        return self.cart_item_repo.get_by_id(cart_id)

    def get_items_by_user(self, cart_id: int) -> list[CartItemModel]:
        return self.cart_item_repo.get_items_cart_user(cart_id)
    
    def get_by_cart(self, cart_id: int) -> CartItemModel:
        return self.cart_item_repo.get_by_id(cart_id)

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

    def delete_item_in_cart(self, cart_item: CartItemModel, item_id: int) -> None:
        self.cart_item_repo.delete_by_id_item(cart_item=cart_item, item_id=item_id)
