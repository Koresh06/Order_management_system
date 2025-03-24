from dataclasses import dataclass
from datetime import datetime

from src.domain.entitys.order import OrderModel


@dataclass
class OrderItemModel:
    id: int
    order_id: int
    item_id: int
    quantity: int
    created_at: datetime
    updated_at: datetime