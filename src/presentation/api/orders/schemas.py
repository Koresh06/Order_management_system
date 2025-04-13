from dataclasses import field
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.domain.entitys.order import OrderStatusEnum
from src.presentation.api.cart_items.schemas import CartItemOutSchema


class OrderBaseSchema(BaseModel):
    user_id: int

class OrderCreateSchema(OrderBaseSchema):
    pass


class OrderOutSchema(OrderBaseSchema):
    id: int
    items: list[CartItemOutSchema]
    status: OrderStatusEnum
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)