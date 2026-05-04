from database.db import get_db_connection
from models.category import Category

class CategoryService:
    """
    Сервіс для роботи з категоріями.
    Повертає об'єкти Category, а не сирі дані з БД.
    """

    @staticmethod
    def get_all():
        # Отримання всіх категорій і перетворення у об'єкти
        conn = get_db_connection()
        try:
            rows = conn.execute("SELECT * FROM categories").fetchall()

            # Перетворюємо записи з БД у об'єкти Category
            categories = [
                Category(row['id'], row['name']) for row in rows
            ]

            return categories

        except Exception:
            return []
        finally:
            conn.close()

    @staticmethod
    def create(name):
        # Створення нової категорії
        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO categories (name) VALUES (?)",
                (name,)
            )
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete(id):
        # Видалення категорії
        conn = get_db_connection()
        try:
            conn.execute(
                "DELETE FROM categories WHERE id = ?",
                (id,)
            )
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()