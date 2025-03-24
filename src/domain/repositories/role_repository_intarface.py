from abc import ABC, abstractmethod
from src.domain.entitys.role import RoleModel


class RoleRepositoryInterface(ABC):

    @abstractmethod
    def create(self, role: RoleModel) -> RoleModel:
        ...

    @abstractmethod
    def get_all(self) -> list[RoleModel]:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> RoleModel:
        ...