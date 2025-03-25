from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ItemModel:
    id: int
    user_id: int
    category_id: int
    name: str
    description: str
    price: float
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
