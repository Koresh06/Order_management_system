from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from src.presentation.api.items.schemas import ItemOutSchema


class CartItemBaseSchema(BaseModel):
    user_id: int


class CartItemCreateSchema(CartItemBaseSchema):
    pass


class CartItemUpdateSchema(BaseModel):
    user_id: int | None = None
    item_id: int | None = None
    quantity: int | None = None


class CartItemUpdatePartialSchema(BaseModel):
    item_id: int | None = None
    quantity: int | None = Field(..., gt=0, lt=100)



class CartItemEntrySchema(BaseModel):
    item: ItemOutSchema
    quantity: int


class CartItemOutSchema(CartItemBaseSchema):
    id: int
    items: list[CartItemEntrySchema]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)