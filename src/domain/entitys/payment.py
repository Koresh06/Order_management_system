from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PaymentModel(BaseModel):
    id: int
    user_id: int
    order_id: int
    amount: float
    status: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
