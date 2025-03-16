from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PaymentModel(BaseModel):
    id: int
    user_id: int
    order_id: int
    amount: float
    payment_date: datetime = datetime.now()
    status: bool

    model_config = ConfigDict(from_attributes=True)
