from abc import ABC, abstractmethod
from src.domain.repositories.base_repository import BaseRepository


class RepositoryFactory(ABC):
    @abstractmethod
    def create_user_repository(self) -> BaseRepository:
        pass

    @abstractmethod
    def create_cart_repository(self) -> BaseRepository:
        pass

    @abstractmethod
    def create_product_repository(self) -> BaseRepository:
        pass

    @abstractmethod
    def create_order_repository(self) -> BaseRepository:
        pass

    # @abstractmethod
    # def create_role_repository(self) -> BaseRepository:
    #     pass
