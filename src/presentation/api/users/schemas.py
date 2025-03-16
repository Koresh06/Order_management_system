from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str


class UserCreateSchema(UserBaseSchema):
    pass


class UserOutSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
