from src.application.services.base_service import BaseService
from src.domain.entitys.product import ProductModel
from src.domain.repositories.base_repository import BaseRepository


class ProductsServiceImpl(BaseService):
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def create(self, product: ProductModel) -> ProductModel:
        return self._repository.create(product)

    def get_all(self) -> list[ProductModel]:
        return self._repository.get_all()

    def get_by_id(self, id: int) -> ProductModel:
        return self._repository.get_by_id(id)

    def update(
        self,
        product: ProductModel,
        product_update: ProductModel,
        partial: bool = False,
    ) -> ProductModel:
        return self._repository.update(
            product=product,
            product_update=product_update,
            partial=partial,
        )

    def delete(self, id: int) -> None:
        return self._repository.delete(id)
