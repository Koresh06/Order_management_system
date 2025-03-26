from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CategoryModel:
    id: int
    user_id: int
    name: str
    description: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)