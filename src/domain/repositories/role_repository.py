from abc import ABC, abstractmethod

from src.domain.entitys.role import Role


class RoleRepositoryABC(ABC):
    @abstractmethod
    def create(self, role: Role) -> Role:
        pass

    @abstractmethod
    def get_all(self) -> list[Role]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Role:
        pass

    @abstractmethod
    def update(self, role: Role) -> Role:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
