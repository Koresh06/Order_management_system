from abc import ABC, abstractmethod

from src.domain.entitys.item import FileDTO


class FileServiceInterface(ABC):

    @abstractmethod
    def save(self, file: FileDTO) -> str:
        pass
