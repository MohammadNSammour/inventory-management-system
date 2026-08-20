import sqlite3
from contextlib import contextmanager
from pathlib import Path
from app.exceptions.database_error import DatabaseError

DATABASE_PATH = Path("data/products.db")

@contextmanager
def get_connection():
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    
    try:
        yield connection
        connection.commit()
    except sqlite3.Error as error:
        if connection is not None:
            connection.rollback()
        raise DatabaseError(f"Database operation failed: {error}") from error
    finally:
        connection.close()

"""
import sqlite3
from pathlib import Path
DATABASE_PATH = Path("data/products.db")
def get_connection() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection
"""