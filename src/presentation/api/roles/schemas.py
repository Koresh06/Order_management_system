from pydantic import BaseModel, ConfigDict


class RoleBaseSchema(BaseModel):
    name: str


class RoleCreateSchema(RoleBaseSchema):
    pass


class RoleUpdateSchema(RoleBaseSchema):
    name: str | None = None


class RoleUpdatePartialSchema(RoleUpdateSchema):
    pass


class RoleOutSchema(RoleBaseSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)
