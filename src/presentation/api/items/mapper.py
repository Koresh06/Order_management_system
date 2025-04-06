from fastapi import UploadFile

from src.domain.entitys.item import FileDTO


def upload_file_to_dto(upload_file: UploadFile) -> FileDTO:
    return FileDTO(
        filename=upload_file.filename,
        content=upload_file.file.read(),
        content_type=upload_file.content_type,
    )
