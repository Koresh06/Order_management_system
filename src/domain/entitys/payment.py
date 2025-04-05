from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entitys.base import BaseModel


@dataclass
class PaymentModel(BaseModel):
    id: int
    user_id: int
    order_id: int
    status: bool
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
