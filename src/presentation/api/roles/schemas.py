from pydantic import BaseModel, ConfigDict


class RoleBaseSchema(BaseModel):
    name: str


class CreateRoleSchema(RoleBaseSchema):
    ...


class UpdateRoleSchema(RoleBaseSchema):
    name: str | None = None


class UpdatePartialRoleSchema(UpdateRoleSchema):
    ...


class RoleOutSchema(RoleBaseSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)