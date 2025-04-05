from datetime import datetime
from src.domain.repositories.item_repository_intarface import ItemRepositoryInterface
from src.domain.entitys.item import ItemModel


class ItemRepositoryImpl(ItemRepositoryInterface):
    def __init__(self):
        self.items = [
            ItemModel(
                id=1,
                user_id=1,
                category_id=1,
                name="Item 1",
                description="Description 1",
                price=10.0,
            ),
            ItemModel(
                id=2,
                user_id=2,
                category_id=2,
                name="Item 2",
                description="Description 2",
                price=20.0,
            )
        ]
        self.counter = 1

    def create(self, item: ItemModel) -> ItemModel:
        new_item = ItemModel(
            id=self.counter,
            user_id=item.user_id,
            category_id=item.category_id,
            name=item.name,
            description=item.description,
            price=item.price,
        )
        self.items.append(new_item)
        return new_item
    
    def get_all(self) -> list[ItemModel]:
        return self.items
    
    def get_by_id(self, id: int) -> ItemModel:
        for item in self.items:
            if item.id == id:
                return item
        return None
    
    def get_by_name(self, name: str) -> ItemModel:
        for item in self.items:
            if item.name == name:
                return item
        return None
    
    def get_items_by_user(self, id: int) -> list[ItemModel]:
        user_items = []
        for item in self.items:
            if item.user_id == id:
                user_items.append(item)
        return user_items
    