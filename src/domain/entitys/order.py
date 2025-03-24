from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OrderStatusEnum(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class OrderModel:
    id: int
    user_id: int
    status: OrderStatusEnum
    total_price: float
    created_at: datetime
    updated_at: datetime
