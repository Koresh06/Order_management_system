from dataclasses import dataclass
from datetime import datetime


@dataclass
class CategoryModel:
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime