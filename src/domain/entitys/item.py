from dataclasses import dataclass
from datetime import datetime


@dataclass
class ItemModel:
    id: int
    user_id: int
    category_id: int
    name: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime
