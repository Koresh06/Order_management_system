from pydantic import ConfigDict

from src.domain.entitys.base import BaseModel
from src.domain.entitys.cart_product import CartProductModel


class CartModel(BaseModel):
    id: int
    user_id: int
    products: list[CartProductModel]
    
    model_config = ConfigDict(from_attributes=True)