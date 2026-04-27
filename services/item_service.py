from database.db import get_db_connection

class ItemService:

    @staticmethod
    def get_all():
        conn = get_db_connection()
        items = conn.execute("SELECT * FROM items").fetchall()
        conn.close()
        return items

    @staticmethod
    def get_by_id(item_id):
        conn = get_db_connection()
        item = conn.execute("SELECT * FROM items WHERE id=?", (item_id,)).fetchone()
        conn.close()
        return item

    @staticmethod
    def create(data):
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO items (name, category, year, price, condition) VALUES (?, ?, ?, ?, ?)",
            (data['name'], data['category'], data['year'], data['price'], data['condition'])
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(item_id, data):
        conn = get_db_connection()
        conn.execute('''
            UPDATE items
            SET name=?, category=?, year=?, price=?, condition=?
            WHERE id=?
        ''', (data['name'], data['category'], data['year'], data['price'], data['condition'], item_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(item_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM items WHERE id=?", (item_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def search(query):
        conn = get_db_connection()
        items = conn.execute(
            "SELECT * FROM items WHERE name LIKE ?",
            ('%' + query + '%',)
        ).fetchall()
        conn.close()
        return items