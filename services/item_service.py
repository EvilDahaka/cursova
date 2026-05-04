from database.db import get_db_connection

class ItemService:

    @staticmethod
    def get_by_user(user_id):
        conn = get_db_connection()
        items = conn.execute("""
            SELECT items.*, categories.name as category_name
            FROM items
            JOIN categories ON items.category_id = categories.id
            WHERE items.user_id = ?
        """, (user_id,)).fetchall()
        conn.close()
        return items

    @staticmethod
    def create(data, user_id):
        conn = get_db_connection()
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
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        conn.execute("DELETE FROM items WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def search(query, user_id):
        conn = get_db_connection()
        items = conn.execute("""
            SELECT items.*, categories.name as category_name
            FROM items
            JOIN categories ON items.category_id = categories.id
            WHERE items.user_id = ?
            AND items.name LIKE ?
            """, (user_id, f"%{query}%")).fetchall()
        conn.close()
        return items
    

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        item = conn.execute(
            "SELECT * FROM items WHERE id = ?",
            (id,)
            ).fetchone()
        conn.close()
        return item
    
    @staticmethod
    def update(id, data):   
        conn = get_db_connection()
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
        conn.close()