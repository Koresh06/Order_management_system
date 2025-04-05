from src.domain.entitys.cart_item import CartItemModel
from src.domain.entitys.user import UserModel
from src.domain.services.item.item_service_interface import ItemServiceInterface
from src.domain.entitys.item import ItemModel
from src.application.utils.error_handlers_utils import ErrorHandlingUtils


class CreateItemUseCase:
    def __init__(self, service: ItemServiceInterface) -> None:
        self.service = service

    def execute(self, item: ItemModel) -> ItemModel:
        try:
            return self.service.create(item)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in CreateItemUseCase", e)
        

class GetAllItemsUseCase:
    def __init__(self, service: ItemServiceInterface) -> None:
        self.service = service

    def execute(self) -> list[ItemModel]:
        try:
            return self.service.get_all()
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in GetAllItemsUseCase", e)
        

class GetAllItemsByUserUseCase:
    def __init__(self, service: ItemServiceInterface) -> None:
        self.service = service

    def execute(self, user: UserModel) -> list[ItemModel]:
        try:
            return self.service.get_all_items_by_user(user.id)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in GetAllItemsByUserUseCase", e)


