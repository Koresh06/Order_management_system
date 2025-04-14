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
    def get_all_orders_by_user(self, user_id: int) -> list[OrderModel]:
        ...

    @abstractmethod
    def get_all_orders(self) -> list[OrderModel]:
        ...

    @abstractmethod
    def delete(self, order_id: int) -> None:
        ...