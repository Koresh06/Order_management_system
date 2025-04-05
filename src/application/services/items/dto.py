from dataclasses import dataclass

from src.domain.entitys.item import ItemModel
from src.domain.entitys.user import UserModel

@dataclass
class GetAllByUserDTO:
    user: UserModel
    items: list[ItemModel]