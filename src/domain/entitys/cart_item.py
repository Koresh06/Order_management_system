from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entitys.base import BaseModel
from src.domain.entitys.item import ItemModel


@dataclass
class CartItemEntryModel(BaseModel):
    item: ItemModel
    quantity: int


@dataclass
class CartItemModel(BaseModel):
    id: int
    user_id: int
    items: list[CartItemEntryModel] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)