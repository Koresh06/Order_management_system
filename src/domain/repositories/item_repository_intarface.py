from abc import ABC, abstractmethod
from src.domain.entitys.item import ItemModel


class ItemRepositoryInterface(ABC):

    @abstractmethod
    def create(self, item: ItemModel) -> ItemModel:
        ...

    @abstractmethod
    def get_all(self) -> list[ItemModel]:
        ...

    @abstractmethod
    def get_all_by_user(self, id: int) -> ItemModel:
        ...