from database.db import get_db_connection

class UserService:
    """
    Сервіс для роботи з користувачами.
    Включає авторизацію, отримання, створення та видалення користувачів.
    """

    @staticmethod
    def login(username, password):
        # Пошук користувача за логіном і паролем
        conn = get_db_connection()
        try:
            user = conn.execute(
                "SELECT * FROM users WHERE username = ? AND password = ?",
                (username, password)
            ).fetchone()
            return user
        except Exception:
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all():
        # Отримання всіх користувачів
        conn = get_db_connection()
        try:
            return conn.execute("SELECT * FROM users").fetchall()
        except Exception:
            return []
        finally:
            conn.close()

    @staticmethod
    def create(username, password, is_admin):
        # Створення нового користувача з роллю
        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
                (username, password, is_admin)
            )
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete(id):
        # Видалення користувача за ID
        conn = get_db_connection()
        try:
            conn.execute("DELETE FROM users WHERE id = ?", (id,))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()