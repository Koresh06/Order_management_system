from abc import ABC, abstractmethod
from src.domain.entitys.item import ItemModel


class ItemRepositoryInterface(ABC):

    @abstractmethod
    def create(self, item: ItemModel, saved_path: str) -> ItemModel:
        ...

    @abstractmethod
    def get_all(self) -> list[ItemModel]:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> ItemModel:
        ...

    @abstractmethod
    def get_by_name(self, name: str) -> ItemModel:
        ...

    @abstractmethod
    def get_items_by_user(self, id: int) -> ItemModel:
        ...