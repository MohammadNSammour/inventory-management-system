from app.exceptions.database_error import DatabaseError
from app.exceptions.product_not_found_error import ProductNotFoundError
from app.exceptions.validation_error import ValidationError
from app.models.product import Product #MODEL
from app.services.product_service import ProductService #SERVICE

class ProductCLI:

    def __init__(self, service: ProductService):
        self.service = service#self means the instance of the class, and service is the parameter passed to the constructor. This line assigns the service parameter to an instance variable self.service, making it accessible throughout the class methods.
        #self itself doesn't have a specific meaning; it's just a convention. You could name it anything, but using self is a widely accepted practice in Python to refer to the instance of the class.
        #and other thing,self doesn't have 'service',but it has 'self.service', which is the instance variable that holds the reference to the ProductService object passed during initialization. This allows the methods of ProductCLI to access the service layer for performing operations related to products.
    
    def run(self):
        while True:
            self._display_menu()
            choice = input("Choose an option: ").strip()
            try:
                if choice == "1":
                    self._create_product()
                elif choice == "2":
                    self._list_products()
                elif choice == "3":
                    self._get_product()
                elif choice == "4":
                    self._update_product()
                elif choice == "5":
                    self._delete_product()
                elif choice == "6":
                    self._search_products()
                elif choice == "7":
                    self._sort_products()
                elif choice == "0":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option.")
            except ValidationError as error:
                print(f"Validation error: {error}")
            except ProductNotFoundError as error:
                print(f"Product not found: {error}")
            except DatabaseError as error:
                print(f"Database error: {error}")

    @staticmethod
    def _display_menu():
        print("\n=== Product Manager ===")
        print("1. Create Product")
        print("2. List Products")
        print("3. Get Product by ID")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Search Products")
        print("7. Sort Products")
        print("0. Exit")

    def _create_product(self):
        name = input("Product name: ").strip()
        price = float(input("Product price: "))
        quantity = int(input("Product quantity: "))
        product = Product(id=None,name=name,price=price,quantity=quantity)
        created_product = self.service.create(product)
        print(f"Product created successfully: {created_product}")

    def _list_products(self):
        products = self.service.list_all()
        if not products:
            print("No products found.")
            return
        for product in products:
            print(product)

    def _get_product(self):
        product_id = int(input("Product ID: "))
        product = self.service.get_by_id(product_id)
        print(product)

    def _update_product(self):
        product_id = int(input("Product ID: "))
        name = input("New product name: ").strip()
        price = float(input("New product price: "))
        quantity = int(input("New product quantity: "))
        product = Product(id=product_id,name=name,price=price,quantity=quantity)
        updated_product = self.service.update(product)
        print(f"Product updated successfully: {updated_product}")

    def _delete_product(self):
        product_id = int(input("Product ID: "))
        self.service.delete(product_id)
        print("Product deleted successfully.")

    def _search_products(self):
        query = input("Search by name: ").strip()
        products = self.service.search(query)
        if not products:
            print("No products found.")
            return
        for product in products:
            print(product)

    def _sort_products(self):
        print("\nSort by:")
        print("1. Name")
        print("2. Price")
        print("3. Quantity")
        choice = input("Choose field: ").strip()
        fields = {
            "1": "name",
            "2": "price",
            "3": "quantity"
        }
        field = fields.get(choice)
        if field is None:
            print("Invalid sort field.")
            return
        order = input("Descending? (y/n): ").strip().lower()
        descending = order == "y"
        products = self.service.sort(field=field,descending=descending)
        if not products:
            print("No products found.")
            return
        for product in products:
            print(product)