from src.domain.repositories.category_repository_intarface import CategoryRepositoryInterface
from src.domain.entitys.category import CategoryModel


class CategoryRepositoryImpl(CategoryRepositoryInterface):
    def __init__(self):
        self.categories = [
            CategoryModel(
                id=1,
                user_id=1,
                name="Category 1",
                description="Description 1",
            )
        ]
        self.counter = 1

    def create(self, category: CategoryModel) -> CategoryModel:
        new_category = CategoryModel(
            id=self.counter,
            user_id=category.user_id,
            name=category.name,
            description=category.description,
        )
        self.categories.append(new_category)
        self.counter += 1
        return new_category

    def get_all(self) -> list[CategoryModel]:
        return self.categories

    def get_by_id(self, id: int) -> CategoryModel:
        for category in self.categories:
            if category.id == id:
                return category
        return None
    
    def get_by_name(self, name: str) -> CategoryModel:
        for category in self.categories:
            if category.name == name:
                return category
        return None
