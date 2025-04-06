from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal

from src.domain.entitys.base import BaseModel


@dataclass
class FileDTO:
    filename: str
    content: bytes
    content_type: str


@dataclass
class ItemModel(BaseModel):
    id: int
    user_id: int
    category_id: int
    name: str
    description: str
    price: Decimal
    image: FileDTO
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
