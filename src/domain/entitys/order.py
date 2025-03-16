from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Order(BaseModel):
    id: int
    user_id: int
    prduct_id: list[int]
    status: str
    total_price: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
