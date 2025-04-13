from abc import ABC, abstractmethod

from src.domain.entitys.order import OrderModel


class OrderServiceInterface(ABC):
    @abstractmethod
    def create(self, order: OrderModel) -> OrderModel:
        ...

    @abstractmethod
    def get_by_id(self, order_id: int) -> OrderModel:
        ...

    @abstractmethod
    def delete(self, order_id: int) -> None:
        ...