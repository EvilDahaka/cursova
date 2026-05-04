# Інформаційна система обліку антикварних товарів

## Опис

Проєкт є інформаційною системою для обліку антикварних товарів магазину.
Система дозволяє зберігати, редагувати, видаляти та шукати інформацію про антикварні предмети.

---

## Функціональні можливості

- Аутентифікація користувачів
- Додавання товарів
- Редагування товарів
- Видалення товарів
- Пошук товарів
- Перегляд списку товарів
- Керування категоріями
- Керування користувачами (для адміністратора)

---

## Використані технології

- Python
- Flask
- SQLite
- HTML (Jinja2)

---

## Структура проєкту

- routes — обробка запитів
- services — бізнес-логіка
- database — робота з базою даних
- templates — інтерфейс користувача

---

## Структура бази даних

### Users
- id
- username
- password
- is_admin

### Categories
- id
- name

### Items
- id
- name
- category_id
- year
- price
- condition
- user_id

---

## Запуск проєкту

1. Створити базу даних:

python database/init_db.py

2. Створити адміністратора:

from database.db import get_db_connection

conn = get_db_connection()
conn.execute("INSERT INTO users (username, password, is_admin) VALUES ('admin', '1234', 1)")
conn.commit()
conn.close()

3. Додати категорії:

from database.db import get_db_connection

conn = get_db_connection()
conn.execute("INSERT INTO categories (name) VALUES ('Картини')")
conn.execute("INSERT INTO categories (name) VALUES ('Монети')")
conn.execute("INSERT INTO categories (name) VALUES ('Скульптури')")
conn.commit()
conn.close()

4. Запустити застосунок:

python run.py

5. Відкрити в браузері:

http://127.0.0.1:5000/login

---

## Дані для входу

Логін: admin
Пароль: 1234

---

## ООП

У проєкті використано:
- інкапсуляцію
- абстракцію
- розділення відповідальності
