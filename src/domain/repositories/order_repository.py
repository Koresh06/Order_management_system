from abc import ABC, abstractmethod

from src.domain.entitys.order import Order


class OrderRepositoryABC(ABC):
    @abstractmethod
    def create(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_all(self) -> list[Order]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Order:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def update(self, order: Order) -> Order:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
