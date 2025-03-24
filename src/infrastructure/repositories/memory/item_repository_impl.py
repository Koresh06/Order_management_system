from datetime import datetime
from src.domain.repositories.item_repository_intarface import ItemRepositoryInterface
from src.domain.entitys.item import ItemModel


class ItemRepositoryImpl(ItemRepositoryInterface):
    def __init__(self):
        self.items = []
        self.counter = 1

    def create(self, item: ItemModel) -> ItemModel:
        new_item = ItemModel(
            id=self.counter,
            user_id=item.user_id,
            category_id=1,
            name=item.name,
            description=item.description,
            price=item.price,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.items.append(new_item)
        return new_item
    
    def get_all(self) -> list[ItemModel]:
        return self.items
    
    def get_all_by_user(self, id: int) -> list[ItemModel]:
        user_items = []
        for item in self.items:
            if item.user_id == id:
                user_items.append(item)
        return user_items
    