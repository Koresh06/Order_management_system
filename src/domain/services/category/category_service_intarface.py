from abc import ABC, abstractmethod

from src.domain.entitys.category import CategoryModel


class CategoryServiceInterface(ABC):

    @abstractmethod
    def create(self, category: CategoryModel) -> CategoryModel:
        ...

    @abstractmethod
    def get_all(self) -> list[CategoryModel]:
        ...