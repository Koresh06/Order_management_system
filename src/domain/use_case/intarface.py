from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

from src.domain.entitys.base import BaseModel

Entity = TypeVar("Entity")


class GenericUseCase(ABC, Generic[Entity]):
    @abstractmethod
    def execute(self) -> Entity:
        """Execute a use case & return an generic type"""


class UseCaseOneEntity(GenericUseCase):
    @abstractmethod
    def execute(self) -> BaseModel:
        """Execute a use case & return an entity object"""


class UseCaseMultipleEntities(GenericUseCase):
    @abstractmethod
    def execute(self) -> Iterable[BaseModel]:
        """Execute a use case & return multiple entity objects"""