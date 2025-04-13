from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from src.domain.entitys.base import BaseModel
from src.domain.entitys.cart_item import CartItemModel


class OrderStatusEnum(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class OrderModel(BaseModel):
    id: int
    user_id: int
    total_price: float
    items: list[CartItemModel] = field(default_factory=list)
    status: OrderStatusEnum = field(default=OrderStatusEnum.PENDING)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
