from abc import ABC, abstractmethod

from src.domain.entitys.item import ItemModel


class ItemServiceInterface(ABC):

    @abstractmethod
    def create(self, item: ItemModel) -> ItemModel:
        ...
    
    @abstractmethod
    def get_all(self) -> list[ItemModel]:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> ItemModel:
        ...

    @abstractmethod
    def get_all_items_by_user(self, user_id: int) -> list[ItemModel]:
        ...