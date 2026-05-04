from database.db import get_db_connection
from models.user import User, AdminUser

class UserService:
    """
    Об'єктний сервіс для роботи з користувачами
    """

    def __init__(self):
        self.get_connection = get_db_connection

    def login(self, username, password):
        # Авторизація користувача
        conn = self.get_connection()
        try:
            row = conn.execute(
                "SELECT * FROM users WHERE username = ? AND password = ?",
                (username, password)
            ).fetchone()

            if not row:
                return None

            # Створюємо об'єкт користувача
            if row['is_admin']:
                return AdminUser(row['id'], row['username'])
            else:
                return User(row['id'], row['username'], False)

        except Exception:
            return None
        finally:
            conn.close()

    def get_all(self):
        # Отримання всіх користувачів як об'єктів
        conn = self.get_connection()
        try:
            rows = conn.execute("SELECT * FROM users").fetchall()

            users = []
            for row in rows:
                if row['is_admin']:
                    users.append(AdminUser(row['id'], row['username']))
                else:
                    users.append(User(row['id'], row['username'], False))

            return users

        except Exception:
            return []
        finally:
            conn.close()

    def create(self, username, password, is_admin):
        # Створення нового користувача
        conn = self.get_connection()
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

    def delete(self, id):
        # Видалення користувача
        conn = self.get_connection()
        try:
            conn.execute("DELETE FROM users WHERE id = ?", (id,))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()