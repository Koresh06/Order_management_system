from abc import abstractmethod
import os

from src.domain.entitys.item import FileDTO
from src.domain.services.item.file_intarface import FileServiceInterface


UPLOAD_FOLDER = "src\presentation\media"

class LocalSaveFileService:
    def __init__(self, base_path: str = UPLOAD_FOLDER):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def save(self, file: FileDTO) -> str:
        # Путь для сохранения файла
        file_path = os.path.join(self.base_path, file.filename)

        # Сохраняем файл локально
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Преобразуем обратные слэши в прямые для веб-пути
        file_path_for_url = file_path.replace(os.sep, '/')

        return file_path_for_url  # Возвращаем путь с прямыми слэшами


