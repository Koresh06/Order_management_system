from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserModel(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
