from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from src.application.containers.container import Container
from src.domain.repositories.role_repository_intarface import RoleRepositoryInterface
from src.presentation.api.roles.schemas import CreateRoleSchema, RoleOutSchema


router = APIRouter(
    prefix="/roles",
    tags=["roles"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RoleOutSchema)
@inject
async def create_role(
    role: CreateRoleSchema,
    repo: Annotated[
        RoleRepositoryInterface,
        Depends(Provide[Container.role_repository]),
    ],
) -> RoleOutSchema:
    return repo.create(role)


@router.get("/", response_model=list[RoleOutSchema])
@inject
async def get_all_roles(
    repo: Annotated[
        RoleRepositoryInterface,
        Depends(Provide[Container.role_repository]),
    ],
) -> list[RoleOutSchema]:
    return repo.get_all()