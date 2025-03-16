from abc import ABC, abstractmethod
from typing import Type, TypeVar, Generic, List, Dict
from src.domain.entitys.base import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def create(self, obj: T) -> T:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> T:
        pass

    @abstractmethod
    def update(self, obj: T, obj_update: T, partial: bool) -> T:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:

        pass
