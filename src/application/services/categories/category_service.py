from src.application.services.categories.exceptions import CategoryAlreadyExistsError
from src.domain.repositories.category_repository_intarface import CategoryRepositoryInterface
from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.entitys.category import CategoryModel

from src.domain.services.category.category_service_intarface import CategoryServiceInterface



class CategoryService(CategoryServiceInterface):
    def __init__(
            self, 
            category_repo: CategoryRepositoryInterface,
    ):
        self.category_repo = category_repo

    def create(self, category: CategoryModel) -> CategoryModel:
        if self.category_repo.get_by_name(category.name) is not None:
            raise CategoryAlreadyExistsError(f"Category ({category.name}) already exists")
        return self.category_repo.create(category)
    
    def get_all(self) -> list[CategoryModel]:
        return self.category_repo.get_all()
    
    