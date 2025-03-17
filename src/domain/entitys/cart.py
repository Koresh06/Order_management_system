from pydantic import ConfigDict

from src.domain.entitys.base import BaseModel
from src.domain.entitys.product import ProductModel


class CartModel(BaseModel):
    id: int
    user_id: int
    product_id: list[ProductModel]
    
    model_config = ConfigDict(from_attributes=True)