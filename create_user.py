from database.db import get_db_connection

conn = get_db_connection()

conn.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ('admin', '1234')
)

conn.commit()
conn.close()

print("Користувач створений!")