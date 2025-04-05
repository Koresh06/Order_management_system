from src.domain.services.item.item_service_interface import ItemServiceInterface
from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.repositories.item_repository_intarface import ItemRepositoryInterface
from src.domain.repositories.category_repository_intarface import CategoryRepositoryInterface
from src.domain.entitys.item import ItemModel
from src.application.services.items.exceptions import CategoryNotFoundError, ItemAlreadyExistsError, UserNotFoundError
from src.application.services.items.dto import GetAllByUserDTO


class ItemService(ItemServiceInterface):

    def __init__(
        self,
        item_repo: ItemRepositoryInterface,
        user_repo: UserRepositoryInterface,
        category_repo: CategoryRepositoryInterface
    ):
        self.item_repo = item_repo
        self.user_repo = user_repo
        self.category_repo = category_repo

    def create(self, item: ItemModel) -> ItemModel:
        if self.user_repo.get_by_id(item.user_id) is None:
            raise UserNotFoundError(f"User with ID ({item.user_id}) does not exist")
        
        if self.category_repo.get_by_id(item.category_id) is None:
            raise CategoryNotFoundError(f"Category with ID ({item.category_id}) does not exist")

        if self.item_repo.get_by_name(item.name) is not None:
            raise ItemAlreadyExistsError(f"Item ({item.name}) already exists")
        
        return self.item_repo.create(item)


    def get_all(self) -> list[ItemModel]:
        return self.item_repo.get_all()
    
    def get_by_id(self, id: int) -> ItemModel:
        return self.item_repo.get_by_id(id)


    def get_all_items_by_user(self, user_id: int) -> GetAllByUserDTO:
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(f"User with ID ({id}) does not exist")
        
        items = self.item_repo.get_items_by_user(user_id)

        return GetAllByUserDTO(user, items)
