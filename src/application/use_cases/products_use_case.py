from src.application.services.base_service import BaseService
from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.entitys.product import ProductModel


class ProductsUseCaseImpl(BaseUseCase):
    def __init__(self, service: BaseService):
        self._service = service

    def create(self, product: ProductModel) ->ProductModel:
        return self._service.create(product)

    def get_all(self) -> list[ProductModel]:
        return self._service.get_all()

    def get_by_id(self, id: int) ->ProductModel:
        return self._service.get_by_id(id)

    def update(
        self,
        product:ProductModel,
        product_update:ProductModel,
        partial: bool = False,
    ) ->ProductModel:
        return self._service.update(
            product=product,
            product_update=product_update,
            partial=partial,
        )

    def delete(self, id: int) -> None:
        return self._service.delete(id)
