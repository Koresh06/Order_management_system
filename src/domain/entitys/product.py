from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    model_config = ConfigDict(from_attributes=True)
