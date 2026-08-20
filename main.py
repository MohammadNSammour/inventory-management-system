###
#ENTRY POINT#
###
from app.cli.product_cli import ProductCLI ###CLI(Interface)
from app.database.initializer import initialize_database ###DB(Initializer)
from app.repositories.product_repository import ProductRepository ###REPO(Database Access Layer)
from app.services.product_service import ProductService ###SERVICE(Business Logic Layer)
from app.validators.product_validator import ProductValidator ###VALIDATOR(Input Validation Layer)

def main():
    initialize_database()

    repository = ProductRepository()
    validator = ProductValidator()
    service = ProductService(repository=repository,validator=validator)
    
    cli = ProductCLI(service)
    cli.run()
###################################
if __name__ == "__main__":
    main()