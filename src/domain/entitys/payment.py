from dataclasses import dataclass
from datetime import datetime


@dataclass
class PaymentModel:
    id: int
    user_id: int
    order_id: int
    amount: float
    status: bool
    created_at: datetime
    updated_at: datetime
