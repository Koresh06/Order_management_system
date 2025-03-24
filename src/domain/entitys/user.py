from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entitys.role import RoleModel



@dataclass
class UserModel:
    id: int
    username: str
    # role: RoleModel
    role_id: int
    email: str
    full_name: str
    password: str
    created_at: datetime
    updated_at: datetime


    def __str__(self) -> str:
        return f"{self.full_name}"
    
    def change_password(self, new_password: str) -> None:
        self.password = new_password
        self.updated_at = datetime.now()

    def check_role(self, role: RoleModel) -> bool:
        return self.role == role

    def update_email(self, new_email: str) -> None:
        self.email = new_email
        self.updated_at = datetime.now()
