from src.application.services.items.item_service_interface import ItemServiceInterface
from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.repositories.item_repository_intarface import ItemRepositoryInterface

from src.domain.entitys.item import ItemModel


class ItemService(ItemServiceInterface):

    def __init__(
        self,
        item_repo: ItemRepositoryInterface,
        user_repo: UserRepositoryInterface,
    ):
        self.item_repo = item_repo
        self.user_repo = user_repo

    def create(self, item: ItemModel) -> ItemModel:
        if self.user_repo.get_by_id(item.user_id) is None:
            raise Exception("User id not found")
        return self.item_repo.create(item)

    def get_all(self) -> list[ItemModel]:
        return self.item_repo.get_all()

    def get_all_by_user(self, id: int) -> ItemModel:
        if self.user_repo.get_by_id(id=id) is None:
            raise Exception("User id not found")
        return self.item_repo.get_all_by_user(id)
