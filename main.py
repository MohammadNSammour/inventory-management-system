from app.cli.product_cli import ProductCLI
from app.database.initializer import initialize_database
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService
from app.validators.product_validator import ProductValidator


def main():
    initialize_database()

    repository = ProductRepository()
    validator = ProductValidator()

    service = ProductService(
        repository=repository,
        validator=validator
    )

    cli = ProductCLI(service)

    cli.run()


if __name__ == "__main__":
    main()