from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PaymentModel:
    id: int
    user_id: int
    order_id: int
    amount: float
    status: bool
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
