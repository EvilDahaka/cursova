from database.db import get_db_connection

class CategoryService:
    """
    Сервіс для роботи з категоріями антикварних предметів.
    """

    @staticmethod
    def get_all():
        # Отримання всіх категорій
        conn = get_db_connection()
        try:
            return conn.execute("SELECT * FROM categories").fetchall()
        except Exception:
            return []
        finally:
            conn.close()

    @staticmethod
    def create(name):
        # Створення нової категорії
        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete(id):
        # Видалення категорії (може не спрацювати якщо є зв’язки)
        conn = get_db_connection()
        try:
            conn.execute("DELETE FROM categories WHERE id = ?", (id,))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()