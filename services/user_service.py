from database.db import get_db_connection

class UserService:

    @staticmethod
    def login(username, password):
        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()
        return user