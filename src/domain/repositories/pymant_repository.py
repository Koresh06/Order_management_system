from abc import ABC, abstractmethod

from src.domain.entitys.payment import PaymentModel


class PaymentRepositoryABC(ABC):
    @abstractmethod
    def create(self, payment: PaymentModel) -> PaymentModel:
        pass

    @abstractmethod
    def get_all(self) -> list[PaymentModel]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> PaymentModel:
        pass

    @abstractmethod
    def update(self, payment: PaymentModel) -> PaymentModel:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
