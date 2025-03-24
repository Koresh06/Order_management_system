from src.domain.repositories.role_repository_intarface import RoleRepositoryInterface
from src.domain.entitys.role import RoleModel


class RoleRepositoryImpl(RoleRepositoryInterface):
    def __init__(self) -> None:
        self.roles = [
            RoleModel(id=1, name="admin"),
            RoleModel(id=2, name="user"),
        ]
        self.counter = 1

    def create(self, role: RoleModel) -> RoleModel:
        new_role = RoleModel(id=self.counter, name=role.name)
        self.roles.append(new_role)
        self.counter += 1
        return new_role
    
    def get_all(self) -> list[RoleModel]:
        return self.roles
    
    def get_by_id(self, id: int) -> RoleModel:
        for role in self.roles:
            if role.id == id:
                return role
        return None