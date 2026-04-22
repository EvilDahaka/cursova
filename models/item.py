class Item:
    def __init__(self, id, name, category, year, price, condition):
        self.id = id
        self.name = name
        self.category = category
        self.year = year
        self.price = price
        self.condition = condition

    @staticmethod
    def get_all(conn):
        return conn.execute("SELECT * FROM items").fetchall()

    @staticmethod
    def get_by_id(conn, id):
        return conn.execute("SELECT * FROM items WHERE id=?", (id,)).fetchone()

    @staticmethod
    def delete(conn, id):
        conn.execute("DELETE FROM items WHERE id=?", (id,))
        conn.commit()