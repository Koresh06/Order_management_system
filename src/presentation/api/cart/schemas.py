from pydantic import BaseModel, ConfigDict


class CartProductBaseSchema(BaseModel):
    cart_id: int
    product_id: int
    quantity: int


class CartBaseSchema(BaseModel):
    user_id: int
    product_id: list[CartProductBaseSchema] = []


class CartCreateSchema(CartBaseSchema):
    pass


class AddCartProductSchema(CartProductBaseSchema):
    pass


class CartOutSchema(CartBaseSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)