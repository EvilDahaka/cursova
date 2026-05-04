from database.db import get_db_connection

class UserService:

    @staticmethod
    def login(username, password):
        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()
        return user

    @staticmethod
    def get_all():
        conn = get_db_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        conn.close()
        return users

    @staticmethod
    def create(username, password):
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        conn.execute("DELETE FROM users WHERE id = ?", (id,))
        conn.commit()
        conn.close()