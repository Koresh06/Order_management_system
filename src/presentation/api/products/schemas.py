from pydantic import BaseModel, ConfigDict


class ProductBaseSchema(BaseModel):
    user_id: int
    name: str
    description: str
    price: float


class ProductCreateSchema(ProductBaseSchema):
    pass


class ProductUpdateSchema(ProductBaseSchema):
    user_id: int | None = None
    name: str | None = None
    description: str | None = None
    price: float | None = None


class ProductUpdatePartilSchema(ProductUpdateSchema):
    pass


class ProductOutSchema(ProductBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)