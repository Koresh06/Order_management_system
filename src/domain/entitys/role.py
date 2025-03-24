from dataclasses import dataclass
from datetime import datetime


@dataclass
class RoleModel:
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
