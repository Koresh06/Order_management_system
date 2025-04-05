from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entitys.base import BaseModel


@dataclass
class CartItemModel(BaseModel):
    id: int
    user_id: int
    item_id: int
    quantity: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)