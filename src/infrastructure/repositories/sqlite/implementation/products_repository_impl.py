from sqlalchemy import select
from src.domain.repositories.base_repository import BaseRepository
from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.models import Product
from src.presentation.api.products.schemas import ProductCreateSchema


class SQLiteProductsRepositoryImpl(BaseRepository):
    def __init__(self, db_helper: SQLiteDatabaseHelper):
        self.db_helper = db_helper

    def create(self, product: ProductCreateSchema) -> Product:
        with self.db_helper.get_session() as session:
            create_product = Product(
                user_id=product.user_id,
                name=product.name,
                description=product.description,
                price=product.price,

            )
            session.add(create_product)
            session.commit()
            session.refresh(create_product)
            return create_product

    def get_all(self) -> list[Product]:
        with self.db_helper.get_session() as session:
            return session.scalars(select(Product)).all()
        

    def get_by_id(self, id: int) -> Product:
        with self.db_helper.get_session() as session:
            return session.get(Product, id)
        
    def update(
        self,
        product: Product,
        product_update: dict,
        partial: bool = False,
    ) -> Product:
        with self.db_helper.get_session() as session:
            product_from_db = session.get(Product, product.id)
            for key, value in product_update.model_dump(exclude_unset=partial).items():
                setattr(product_from_db, key, value)
            session.commit()
            session.refresh(product_from_db)
            return product_from_db

    def delete(self, id: int) -> None:
        with self.db_helper.get_session() as session:
            product = session.get(Product, id)
            session.delete(product)
            session.commit()
        
    