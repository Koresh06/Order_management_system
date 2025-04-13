from dependency_injector import containers, providers

from src.application.services.cart_item.cart_item_service import CartItemService
from src.application.services.categories.category_service import CategoryService
from src.application.services.items.item_service import ItemService
from src.application.services.items.save_file import LocalSaveFileService
from src.application.services.orders.order_service import OrderService
from src.application.services.users.security import PasswordHasher
from src.application.services.users.user_service import UserService
from src.application.use_cases.cart_item_use_case import AddCartItemUseCase, DeleteItemInCartUseCase, GetAllItemsInUserCartUseCase, UpdateItemInCartUseCase
from src.application.use_cases.category_use_case import CreateCategoryUseCase
from src.application.use_cases.item_use_case import CreateItemUseCase, GetAllItemsByUserUseCase, GetAllItemsUseCase
from src.application.use_cases.order_use_case import CreateOrderUseCase
from src.application.use_cases.user_use_case import DeleteUserUseCase, GetAllUsersUseCase, RegisterUserUseCase
from src.infrastructure.external_services.send_email import EmailService
from src.infrastructure.repositories.memory.cart_item_repository_impl import CartItemRepositoryImpl
from src.infrastructure.repositories.memory.category_repository_impl import CategoryRepositoryImpl
from src.infrastructure.repositories.memory.item_repository_impl import ItemRepositoryImpl
from src.infrastructure.repositories.memory.order_repository_impl import OrderRepositoryImpl
from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl





class MainContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    #users module
    user_repo = providers.Singleton(UserRepositoryImpl)
    password_hasher = providers.Singleton(PasswordHasher)
    email_service = providers.Singleton(EmailService)

    user_service = providers.Singleton(
        UserService,
        user_repo=user_repo,
        password_hasher=password_hasher,
        email_service=email_service,
    )

    register_user_use_case = providers.Factory(
        RegisterUserUseCase,
        service=user_service,
    )
    get_all_users_use_case = providers.Factory(
        GetAllUsersUseCase,
        service=user_service,
    )
    delete_user_use_case = providers.Factory(
        DeleteUserUseCase,
        service=user_service,
    )

    #categories module
    category_repo = providers.Singleton(CategoryRepositoryImpl)
    
    category_service = providers.Singleton(
        CategoryService,
        category_repo=category_repo,
        user_repo=user_repo,
    )

    create_category_use_case = providers.Factory(
        CreateCategoryUseCase,
        service=category_service,
    )

    #items module
    item_repo = providers.Singleton(ItemRepositoryImpl)
    file_service = providers.Singleton(LocalSaveFileService)

    item_service = providers.Singleton(
        ItemService,
        item_repo=item_repo,
        user_repo=user_repo,
        category_repo=category_repo,
        file_service=file_service,
    )

    create_item_use_case = providers.Factory(
        CreateItemUseCase,
        service=item_service,
    )
    get_all_items_use_case = providers.Factory(
        GetAllItemsUseCase,
        service=item_service,

    )
    get_all_items_by_user_use_case = providers.Factory(
        GetAllItemsByUserUseCase,
        service=item_service,
    )

    #cart_item module
    cart_item_repo = providers.Singleton(CartItemRepositoryImpl)

    cart_item_service = providers.Singleton(
        CartItemService,
        cart_item_repo=cart_item_repo,
        user_repo=user_repo,
        item_repo=item_repo,
    )

    add_cart_item_use_case = providers.Factory(
        AddCartItemUseCase,
        service=cart_item_service,
    )

    get_all_by_cart_user = providers.Factory(
        GetAllItemsInUserCartUseCase,
        service=cart_item_service,
    )

    update_item_in_cart_use_case = providers.Factory(
        UpdateItemInCartUseCase,
        service=cart_item_service,
    )
    
    delete_item_in_cart_use_case = providers.Factory(
        DeleteItemInCartUseCase,
        service=cart_item_service,
    )

    #order module
    order_repo = providers.Singleton(OrderRepositoryImpl)

    order_service = providers.Singleton(
        OrderService,
        order_repo=order_repo,
        cart_item_repo=cart_item_repo,
    )

    create_order_use_case = providers.Factory(
        CreateOrderUseCase,
        order_service=order_service,
    )
