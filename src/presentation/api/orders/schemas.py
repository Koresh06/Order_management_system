from pydantic import BaseModel, ConfigDict


class OrderBaseSchema(BaseModel):
    user_id: int
    status: str
    total_price: float


class OrderCreateSchema(OrderBaseSchema):
    pass


class OrderUpdateSchema(OrderBaseSchema):
    user_id: int | None = None
    status: str | None = None
    total_price: float | None = None


class OrderUpdatePartilSchema(BaseModel):
    pass


class OrderOutSchema(OrderBaseSchema):
    id: int
    products: list = []

    model_config = ConfigDict(from_attributes=True)