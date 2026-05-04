from database.db import get_db_connection
from models.category import Category

class CategoryService:
    """
    Об'єктний сервіс для роботи з категоріями
    """

    def __init__(self):
        # Інкапсуляція доступу до БД
        self.get_connection = get_db_connection

    def get_all(self):
        # Отримання категорій як об'єктів
        conn = self.get_connection()
        try:
            rows = conn.execute("SELECT id, name FROM categories").fetchall()

            return [Category(row['id'], row['name']) for row in rows]

        except Exception:
            return []
        finally:
            conn.close()

    def create(self, name):
        # Бізнес-логіка + валідація
        if not name or len(name.strip()) < 2:
            raise ValueError("Назва категорії некоректна")

        conn = self.get_connection()
        try:
            conn.execute(
                "INSERT INTO categories (name) VALUES (?)",
                (name.strip(),)
            )
            conn.commit()
            return True

        except Exception:
            return False
        finally:
            conn.close()

    def delete(self, category_id):
        conn = self.get_connection()
        try:
            conn.execute(
                "DELETE FROM categories WHERE id = ?",
                (category_id,)
            )
            conn.commit()
            return True

        except Exception:
            return False
        finally:
            conn.close()