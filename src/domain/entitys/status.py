from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StatusModel(BaseModel):
    id: int
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    model_config = ConfigDict(from_attributes=True)
