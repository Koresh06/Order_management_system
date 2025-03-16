from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductModel(BaseModel):
    id: int
    user_id: int
    name: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
