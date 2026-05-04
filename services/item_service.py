from database.db import get_db_connection
from models.item import Item

class ItemService:
    """
    Сервіс для роботи з антикварними товарами.
    Працює з об'єктами Item та інкапсулює логіку доступу до БД.
    """

    def __init__(self):
        # Зберігаємо функцію підключення до БД
        self.get_connection = get_db_connection

    def get_by_user(self, user_id):
        # Отримання всіх товарів конкретного користувача
        conn = self.get_connection()
        try:
            rows = conn.execute("""
                SELECT items.*, categories.name as category_name
                FROM items
                JOIN categories ON items.category_id = categories.id
                WHERE items.user_id = ?
            """, (user_id,)).fetchall()

            # Перетворення рядків БД у об'єкти Item
            return [
                Item(
                    row['id'],
                    row['name'],
                    row['category_id'],
                    row['year'],
                    row['price'],
                    row['condition'],
                    row['user_id'],
                    row['category_name']
                )
                for row in rows
            ]

        except Exception:
            return []
        finally:
            conn.close()

    def get_by_id(self, id):
        # Отримання одного товару за ID
        conn = self.get_connection()
        try:
            row = conn.execute(
                "SELECT * FROM items WHERE id = ?",
                (id,)
            ).fetchone()

            if not row:
                return None

            return Item(
                row['id'],
                row['name'],
                row['category_id'],
                row['year'],
                row['price'],
                row['condition'],
                row['user_id']
            )

        except Exception:
            return None
        finally:
            conn.close()

    def create(self, data, user_id):
        # Додавання нового товару
        conn = self.get_connection()
        try:
            conn.execute("""
                INSERT INTO items (name, category_id, year, price, condition, user_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data['name'],
                data['category_id'],
                data['year'],
                data['price'],
                data['condition'],
                user_id
            ))
            conn.commit()
            return True

        except Exception:
            return False
        finally:
            conn.close()

    def update(self, id, data):
        # Оновлення існуючого товару
        conn = self.get_connection()
        try:
            conn.execute("""
                UPDATE items
                SET name = ?, category_id = ?, year = ?, price = ?, condition = ?
                WHERE id = ?
            """, (
                data['name'],
                data['category_id'],
                data['year'],
                data['price'],
                data['condition'],
                id
            ))
            conn.commit()
            return True

        except Exception:
            return False
        finally:
            conn.close()

    def delete(self, id):
        # Видалення товару за ID
        conn = self.get_connection()
        try:
            conn.execute("DELETE FROM items WHERE id = ?", (id,))
            conn.commit()
            return True

        except Exception:
            return False
        finally:
            conn.close()

    def search(self, query, user_id):
        # Пошук товарів за назвою
        conn = self.get_connection()
        try:
            rows = conn.execute("""
                SELECT items.*, categories.name as category_name
                FROM items
                JOIN categories ON items.category_id = categories.id
                WHERE items.name LIKE ? AND items.user_id = ?
            """, ('%' + query + '%', user_id)).fetchall()

            # Перетворення результату у об'єкти Item
            return [
                Item(
                    row['id'],
                    row['name'],
                    row['category_id'],
                    row['year'],
                    row['price'],
                    row['condition'],
                    row['user_id'],
                    row['category_name']
                )
                for row in rows
            ]

        except Exception:
            return []
        finally:
            conn.close()