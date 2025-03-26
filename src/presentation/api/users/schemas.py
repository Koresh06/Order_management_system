from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

from src.presentation.api.roles.schemas import RoleOutSchema


class UserBaseSchema(BaseModel):
    username: str
    role_id: int
    email: str
    full_name: str
    password: str


class UserCreateSchema(UserBaseSchema):
    pass


class UserUpdateSchema(UserBaseSchema):
    username: str | None = None
    email: str | None = None
    full_name: str | None = None
    password: str | None = None


class UserUpdatePartialSchema(UserUpdateSchema):
    pass


class UserOutSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
