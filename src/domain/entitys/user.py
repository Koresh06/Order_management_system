from dataclasses import dataclass
from datetime import datetime

from src.domain.entitys.role import RoleModel


@dataclass
class UserModel:
    id: int
    username: str
    email: str
    password: str
    role: RoleModel
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

