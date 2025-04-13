from src.domain.use_case.intarface import UseCaseOneEntity, UseCaseMultipleEntities
from src.domain.entitys.order import OrderModel
from src.domain.services.order.order_service_intarface import OrderServiceInterface
from src.application.utils.error_handlers_utils import ErrorHandlingUtils


class CreateOrderUseCase(UseCaseOneEntity):
    def __init__(
        self,
        order_service: OrderServiceInterface,
    ) -> None:
        self.order_service = order_service

    def execute(self, order: OrderModel) -> OrderModel:
        try:
            return self.order_service.create(order.user_id)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in CreateOrderUseCase", e)


class CancelOrderUseCase(UseCaseOneEntity):
    def __init__(
        self,
        order_service: OrderServiceInterface,
    ) -> None:
        self.order_service = order_service
    
    def execute(self, order: OrderModel) -> None:
        try:
            return self.order_service.delete(order.id)
        except Exception as e:
            raise ErrorHandlingUtils.application_error("Error in CancelOrderUseCase", e)