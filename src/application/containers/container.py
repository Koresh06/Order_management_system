from dependency_injector import containers, providers

from src.infrastructure.repositories.memory.user_repository_impl import UserRepositoryImpl
from src.infrastructure.repositories.memory.role_repository_impl import RoleRepositoryImpl
from src.infrastructure.repositories.memory.item_repository_impl import ItemRepositoryImpl
from src.infrastructure.repositories.memory.category_repository_impl import CategoryRepositoryImpl
from src.infrastructure.repositories.memory.cart_item_repository_impl import CartItemRepositoryImpl

from src.application.services.users.user_service import UserService
from src.application.services.items.item_service import ItemService
from src.application.services.categories.category_service import CategoryService
from src.application.services.cart_item.cart_item_service import CartItemService



class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repository = providers.Singleton(UserRepositoryImpl)
    role_repository = providers.Singleton(RoleRepositoryImpl)
    item_repository = providers.Singleton(ItemRepositoryImpl)
    category_repository = providers.Singleton(CategoryRepositoryImpl)
    cart_item_repository = providers.Singleton(CartItemRepositoryImpl)


    user_service = providers.Factory(
        UserService,
        user_repo=user_repository, 
        role_repo=role_repository   
    )
    
    category_service = providers.Factory(
        CategoryService,
        category_repo=category_repository,
        user_repo=user_repository,
    )

    item_service = providers.Factory(
        ItemService,
        item_repo=item_repository,
        user_repo=user_repository
    )

    cart_item_service = providers.Factory(
        CartItemService,
        cart_item_repo=cart_item_repository,
    )