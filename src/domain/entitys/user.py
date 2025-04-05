from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entitys.base import BaseModel
from src.domain.entitys.role import RoleEnum

@dataclass
class UserModel(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    password: str
    role: RoleEnum = field(default=RoleEnum.USER)
    is_active: bool = field(default=False)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


    def __str__(self) -> str:
        return f"{self.full_name}"
    
    def change_password(self, new_password: str) -> None:
        self.password = new_password
        self.updated_at = datetime.now()

    def update_email(self, new_email: str) -> None:
        self.email = new_email
        self.updated_at = datetime.now()
