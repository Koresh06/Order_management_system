from abc import ABC, abstractmethod

from src.domain.entitys.role import RoleModel


class RoleRepositoryABC(ABC):
    @abstractmethod
    def create(self, role: RoleModel) -> RoleModel:
        pass

    @abstractmethod
    def get_all(self) -> list[RoleModel]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> RoleModel:
        pass

    @abstractmethod
    def update(self, role: RoleModel) -> RoleModel:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
