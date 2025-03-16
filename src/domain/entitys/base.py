from pydantic import BaseModel, ConfigDict
from typing import Optional

class BaseModel(BaseModel):
    id: Optional[int]

    model_config = ConfigDict(from_attributes=True)