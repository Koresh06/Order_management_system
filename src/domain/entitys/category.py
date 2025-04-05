from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entitys.base import BaseModel


@dataclass
class CategoryModel(BaseModel):
    id: int
    user_id: int
    name: str
    description: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)