from app.database.connection import get_connection
from app.models.product import Product


class ProductRepository:

    def create(self, product: Product) -> Product:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO products (name, price, quantity)
                VALUES (?, ?, ?)
                """,
                (product.name, product.price, product.quantity)
            )

            product.id = cursor.lastrowid

        return product

    def get_by_id(self, product_id: int) -> Product | None:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT id, name, price, quantity
                FROM products
                WHERE id = ?
                """,
                (product_id,)
            )

            row = cursor.fetchone()

        if row is None:
            return None

        return Product(
            id=row["id"],
            name=row["name"],
            price=row["price"],
            quantity=row["quantity"]
        )
    
    def list_all(self) -> list[Product]:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT id, name, price, quantity
                FROM products
                """
            )

            rows = cursor.fetchall()

        return [
            Product(
                id=row["id"],
                name=row["name"],
                price=row["price"],
                quantity=row["quantity"]
            )
            for row in rows
        ]
    
    def update(self, product: Product) -> bool:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE products
                SET name = ?, price = ?, quantity = ?
                WHERE id = ?
                """,
                (
                    product.name,
                    product.price,
                    product.quantity,
                    product.id
                )
            )

        return cursor.rowcount > 0

    def delete(self, product_id: int) -> bool:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                DELETE FROM products
                WHERE id = ?
                """,
                (product_id,)
            )

            return cursor.rowcount > 0

    def search(self, query: str) -> list[Product]:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT id, name, price, quantity
                FROM products
                WHERE LOWER(name) LIKE LOWER(?)
                """,
                (f"%{query}%",)
            )

            rows = cursor.fetchall()

        return [
            Product(
                id=row["id"],
                name=row["name"],
                price=row["price"],
                quantity=row["quantity"]
            )
            for row in rows
        ]
    
    def sort(self, field: str, descending: bool = False) -> list[Product]:
        allowed_fields = {"name", "price", "quantity"}

        if field not in allowed_fields:
            raise ValueError(f"Invalid sort field: {field}")

        direction = "DESC" if descending else "ASC"

        with get_connection() as connection:
            cursor = connection.execute(
                f"""
                SELECT id, name, price, quantity
                FROM products
                ORDER BY {field} {direction}
                """
            )

            rows = cursor.fetchall()

        return [
            Product(
                id=row["id"],
                name=row["name"],
                price=row["price"],
                quantity=row["quantity"]
            )
            for row in rows
        ]