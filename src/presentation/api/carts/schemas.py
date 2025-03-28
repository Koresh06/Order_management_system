from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CartItemBaseSchema(BaseModel):
    user_id: int
    item_id: int
    quantity: int


class CartItemCreateSchema(CartItemBaseSchema):
    pass


class CartItemUpdateSchema(CartItemBaseSchema):
    user_id: int | None = None
    item_id: int | None = None
    quantity: int | None = None


class CartItemUpdatePartialSchema(BaseModel):
    item_id: int | None = None
    quantity: int | None = Field(..., gt=0, lt=100)



class CartItemOutSchema(CartItemBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)