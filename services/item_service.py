from database.db import get_db_connection

class ItemService:
    """
    Сервіс для роботи з антикварними товарами.
    """

    @staticmethod
    def get_by_user(user_id):
        # Отримання товарів конкретного користувача з назвами категорій
        conn = get_db_connection()
        try:
            items = conn.execute("""
                SELECT items.*, categories.name as category_name
                FROM items
                JOIN categories ON items.category_id = categories.id
                WHERE items.user_id = ?
            """, (user_id,)).fetchall()
            return items
        except Exception:
            return []
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        # Отримання одного товару за ID
        conn = get_db_connection()
        try:
            item = conn.execute(
                "SELECT * FROM items WHERE id = ?",
                (id,)
            ).fetchone()
            return item
        except Exception:
            return None
        finally:
            conn.close()

    @staticmethod
    def create(data, user_id):
        # Додавання нового товару
        conn = get_db_connection()
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

    @staticmethod
    def delete(id):
        # Видалення товару
        conn = get_db_connection()
        try:
            conn.execute("DELETE FROM items WHERE id = ?", (id,))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def update(id, data):
        # Оновлення даних товару
        conn = get_db_connection()
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

    @staticmethod
    def search(query, user_id):
        # Пошук товарів за назвою
        conn = get_db_connection()
        try:
            items = conn.execute("""
                SELECT items.*, categories.name as category_name
                FROM items
                JOIN categories ON items.category_id = categories.id
                WHERE items.name LIKE ? AND items.user_id = ?
            """, ('%' + query + '%', user_id)).fetchall()
            return items
        except Exception:
            return []
        finally:
            conn.close()