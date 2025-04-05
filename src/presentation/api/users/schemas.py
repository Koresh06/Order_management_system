from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from src.domain.entitys.role import RoleEnum


class UserBaseSchema(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=3, max_length=100)


class UserCreateSchema(UserBaseSchema):
    password: str = Field(..., min_length=8, max_length=100)
    role: RoleEnum = RoleEnum.USER 


class UserUpdateSchema(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=50)
    email: EmailStr | None = None
    full_name: str | None = Field(None, min_length=3, max_length=100)
    password: str | None = Field(None, min_length=8, max_length=100)


class UserUpdatePartialSchema(UserUpdateSchema):
    model_config = ConfigDict(from_attributes=True)


class UserOutSchema(UserBaseSchema):
    id: int
    role: RoleEnum
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PaginationQueryParams(BaseModel):
    limit: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Максимум 100 пользователей за раз"
    )
    offset: int = Field(
        default=0,
        ge=0,
        description="Смещение от начала списка"
    )