from abc import ABC, abstractmethod

from src.domain.entitys.status import Status


class StatusRepositoryABC(ABC):
    @abstractmethod
    def create(self, status: Status) -> Status:
        pass

    @abstractmethod
    def get_all(self) -> list[Status]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Status:
        pass

    @abstractmethod
    def update(self, status: Status) -> Status:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
