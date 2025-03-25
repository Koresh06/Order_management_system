from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entitys.order import OrderModel


@dataclass
class OrderItemModel:
    id: int
    order_id: int
    item_id: int
    quantity: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)