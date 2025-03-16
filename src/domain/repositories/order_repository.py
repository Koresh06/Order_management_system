from abc import ABC, abstractmethod

from src.domain.entitys.order import OrderModel


class OrderRepositoryABC(ABC):
    @abstractmethod
    def create(self, order: OrderModel) -> OrderModel:
        pass

    @abstractmethod
    def get_all(self) -> list[OrderModel]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> OrderModel:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def update(self, order: OrderModel) -> OrderModel:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
