from abc import ABC, abstractmethod

from src.domain.entitys.ProductModel import ProductModel


class ProductRepositoryABC(ABC):
    @abstractmethod
    def create(self, product: ProductModel) -> ProductModel:
        pass

    @abstractmethod
    def get_all(self) -> list[ProductModel]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> ProductModel:
        pass

    @abstractmethod
    def update(self, product: ProductModel) -> ProductModel:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
