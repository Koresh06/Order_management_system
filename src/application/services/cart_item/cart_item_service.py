from datetime import datetime
from src.application.services.cart_item.calculate_total_price import CartItemPriceCalculator
from src.application.services.cart_item.exceptions import CartItemAlreadyExistsError, ItemNotFoundError
from src.application.services.items.exceptions import UserNotFoundError
from src.application.services.orders.exceptions import CartItemNotFoundError
from src.domain.entitys.cart_item import CartItemModel, CartItemEntryModel
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

    def add_item(self, user_id: int, item_id: int, quantity: int) -> CartItemModel:
        if self.user_repo.get_by_id(user_id) is None:
            raise UserNotFoundError(f"User with ID ({user_id}) does     not exist")

        item = self.item_repo.get_by_id(item_id)
        if item is None:
            raise ItemNotFoundError(f"Item with ID ({item_id}) does not exist")

        cart = self.cart_item_repo.get_cart_by_id_user(user_id)

        cart_item_entry = CartItemEntryModel(item=item, quantity=quantity)

        if cart is None:
            new_cart_item = CartItemModel(
                id=0,
                user_id=user_id,
                items=[cart_item_entry],
                total_price=item.price * quantity,
            )
            return self.cart_item_repo.create_cart_item(new_cart_item)

        if self.cart_item_repo.get_item_in_cart(user_id=user_id, item_id=item_id) is not None:
            raise CartItemAlreadyExistsError("Cart item already exists  in the cart")

        cart.total_price = CartItemPriceCalculator.calculate_total_price(cart)

        return self.cart_item_repo.add(
            cart_item=cart,
            cart_entry_item=cart_item_entry,
        )


    def get_items_by_user(self, user_id: int) -> list[CartItemModel]:
        if self.cart_item_repo.get_cart_by_id_user(user_id) is None:
            raise CartItemNotFoundError("Cart is empty")
        
        return self.cart_item_repo.get_cart_by_id_user(user_id)

    def update_cart_quantity(
        self,
        cart_item: CartItemModel,
        item_id: int,
        quantity: int,
    ) -> CartItemModel:
        updated_cart = self.cart_item_repo.update_cart_item(
            cart_item=cart_item,
            item_id=item_id,
            updated_data={"quantity": quantity},
        )
        updated_cart.total_price = CartItemPriceCalculator.calculate_total_price(updated_cart)
        updated_cart.updated_at = datetime.now()
        return updated_cart

    def delete_item_in_cart(
        self,
        cart_item: CartItemModel,
        item_id: int,
    ) -> None:
        self.cart_item_repo.delete_by_id_item(
            cart_item=cart_item,
            item_id=item_id,
        )
        cart_item.total_price = CartItemPriceCalculator.calculate_total_price(cart_item)
        cart_item.updated_at = datetime.now()
