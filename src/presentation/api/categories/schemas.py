from pydantic import BaseModel, ConfigDict  


class CategoryBaseSchema(BaseModel):
    user_id: int
    name: str
    description: str


class CategoryCreateSchema(CategoryBaseSchema):
    pass


class CategoryUpdateSchema(CategoryBaseSchema):
    user_id: int | None = None
    name: str | None = None
    description: str | None = None


class CategoryUpdatePartialSchema(CategoryUpdateSchema):
    pass


class CategoryOutSchema(CategoryBaseSchema):
    id: int
    
    model_config = ConfigDict(from_attributes=True)