from dataclasses import dataclass, field
from datetime import datetime



@dataclass
class UserModel:
    id: int
    username: str
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

    def check_role(self, role_id: int) -> bool:
        return self.role_id == role_id

    def update_email(self, new_email: str) -> None:
        self.email = new_email
        self.updated_at = datetime.now()
