from src.application.utils.error_handlers_utils import ErrorHandlingUtils
from src.domain.entitys.cart_item import CartItemModel
from src.domain.use_case.intarface import UseCaseOneEntity, UseCaseMultipleEntities
from src.domain.services.cart_item.cart_item_service_intarface import CartItemServiceInterface


class AddCartItemUseCase(UseCaseOneEntity):
    def __init__(self, service: CartItemServiceInterface):
        self.service = service

    def execute(self, cart_item: CartItemModel, item_id: int, quantity: int) -> CartItemModel:
        try:
            return self.service.add_item(cart_item=cart_item, item_id=item_id, quantity=quantity)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in AddCartItemUseCase", e)


class GetAllItemsInUserCartUseCase(UseCaseMultipleEntities):
    def __init__(self, service: CartItemServiceInterface):
        self.service = service

    def execute(self, user_id: int) -> list[CartItemModel]:
        try:
            return self.service.get_items_by_user(user_id)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in GetAllItemsInUserCartUseCase", e)


class UpdateItemInCartUseCase(UseCaseOneEntity):
    def __init__(self, service: CartItemServiceInterface):
        self.service = service

    def execute(
        self,
        cart_item: CartItemModel,
        item_id: int,
        quantity: int,
    ) -> CartItemModel:
        try:
            return self.service.update_cart_quantity(
                cart_item=cart_item,
                item_id=item_id,
                quantity=quantity,
            )
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in UpdateItemInCartUseCase", e)


class DeleteItemInCartUseCase(UseCaseOneEntity):
    def __init__(self, service: CartItemServiceInterface):
        self.service = service

    def execute(self, cart_item: CartItemModel, item_id: int) -> None:
        try:
            self.service.delete_item_in_cart(cart_item=cart_item, item_id=item_id)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in DeleteItemInCartUseCase", e)