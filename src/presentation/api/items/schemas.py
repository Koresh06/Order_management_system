from datetime import datetime
from pydantic import BaseModel, ConfigDict  

from src.presentation.api.users.schemas import UserOutSchema


class ItemBaseSchema(BaseModel):
    user_id: int
    category_id: int
    name: str
    description: str
    price: float


class ItemCreateSchema(ItemBaseSchema):
    pass


class UpdateItemSchema(ItemBaseSchema):
    user_id: int | None = None
    category_id: int | None = None
    name: str | None = None
    description: str | None = None
    price: float | None = None


class UpdatePartialItemSchema(UpdateItemSchema):
    pass


class ItemOutSchema(ItemBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class GetAllByUserSchema(BaseModel):
    user: UserOutSchema  
    items: list[ItemOutSchema]

    model_config = ConfigDict(from_attributes=True)