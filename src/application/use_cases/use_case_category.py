from src.application.utils.error_handlers_utils import ErrorHandlingUtils
from src.domain.use_case.intarface import UseCaseOneEntity
from src.domain.entitys.category import CategoryModel
from src.domain.services.category.category_service_intarface import CategoryServiceInterface



class CreateCategoryUseCase(UseCaseOneEntity):
    def __init__(self, service: CategoryServiceInterface) -> None:
        self.service = service

    def execute(self, category: CategoryModel) -> CategoryModel:
        try:
            return self.service.create(category)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in CreateCategoryUseCase", e)
