from app.exceptions.validation_error import ValidationError
from app.models.product import Product

class ProductValidator:

    @staticmethod
    def validate(product: Product) -> None:
        if not product.name.strip():
            raise ValidationError("Product name cannot be empty.")
        if product.price < 0:
            raise ValidationError("Product price cannot be negative.")
        if product.quantity < 0:
            raise ValidationError("Product quantity cannot be negative.")