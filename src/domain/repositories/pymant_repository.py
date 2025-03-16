from abc import ABC, abstractmethod

from src.domain.entitys.payment import Payment


class PaymentRepositoryABC(ABC):
    @abstractmethod
    def create(self, payment: Payment) -> Payment:
        pass

    @abstractmethod
    def get_all(self) -> list[Payment]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Payment:
        pass

    @abstractmethod
    def update(self, payment: Payment) -> Payment:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
