from datetime import datetime
from decimal import Decimal
from typing import Annotated
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, ConfigDict  

from src.presentation.api.users.schemas import UserOutSchema


class ItemBaseSchema(BaseModel):
    user_id: int
    category_id: int
    name: str
    description: str
    price: Decimal


class ItemCreateSchema(ItemBaseSchema):
    image: Annotated[UploadFile, File()]

    @classmethod
    def as_form(
        cls,
        user_id: int = Form(...),
        category_id: int = Form(...),
        name: str = Form(...),
        description: str = Form(...),
        price: Decimal = Form(...),
        image: UploadFile = File(...),
    ) -> "ItemCreateSchema":
        return cls(
            user_id=user_id,
            category_id=category_id,
            name=name,
            description=description,
            price=price,
            image=image,
        )



class UpdateItemSchema(ItemBaseSchema):
    user_id: int | None = None
    category_id: int | None = None
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    image: str | None = None


class UpdatePartialItemSchema(UpdateItemSchema):
    pass


class ItemOutSchema(ItemBaseSchema):
    id: int
    image: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class GetAllByUserSchema(BaseModel):
    user: UserOutSchema  
    items: list[ItemOutSchema]

    model_config = ConfigDict(from_attributes=True)