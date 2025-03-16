from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Payment(BaseModel):
    id: int
    oder_id: int
    user_id: int
    amount: float
    payment_date: datetime
    status: bool

    model_config = ConfigDict(from_attributes=True)
