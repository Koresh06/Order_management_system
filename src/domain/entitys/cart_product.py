from pydantic import ConfigDict

from src.domain.entitys.base import BaseModel


class CartProductModel(BaseModel):
    product_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)