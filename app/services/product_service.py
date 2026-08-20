from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.validators.product_validator import ProductValidator
from app.exceptions.product_not_found_error import ProductNotFoundError

class ProductService:

    def __init__(
        self,
        repository: ProductRepository,
        validator: ProductValidator
    ):
        self.repository = repository
        self.validator = validator

    def create(self, product: Product) -> Product:
        self.validator.validate(product)

        return self.repository.create(product)

    def get_by_id(self, product_id: int) -> Product | None:
        product = self.repository.get_by_id(product_id)
        if product is None:
            raise ProductNotFoundError(
                f"Product with ID {product_id} was not found."
            )
        return product

    def list_all(self) -> list[Product]:
        return self.repository.list_all()

    def update(self, product: Product) -> Product:
        self.validator.validate(product)

        existing_product = self.repository.get_by_id(product.id)

        if existing_product is None:
            raise ProductNotFoundError(
                f"Product with ID {product.id} was not found."
            )

        self.repository.update(product)

        return product

    def delete(self, product_id: int) -> None:
        existing_product = self.repository.get_by_id(product_id)

        if existing_product is None:
            raise ProductNotFoundError(
                f"Product with ID {product_id} was not found."
            )

        self.repository.delete(product_id)

    def search(self, query: str) -> list[Product]:
        return self.repository.search(query)

    def sort(
        self,
        field: str,
        descending: bool = False
    ) -> list[Product]:
        return self.repository.sort(field, descending)