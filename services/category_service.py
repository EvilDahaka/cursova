from database.db import get_db_connection

class CategoryService:

    @staticmethod
    def get_all():
        conn = get_db_connection()
        categories = conn.execute("SELECT * FROM categories").fetchall()
        conn.close()
        return categories

    @staticmethod
    def create(name):
        conn = get_db_connection()
        conn.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        conn.execute("DELETE FROM categories WHERE id = ?", (id,))
        conn.commit()
        conn.close()