from run import app
from extensions import db

from models.painting import Painting
from models.category import Category


with app.app_context():

    # Створення категорії
    category = Category(
        name="Картини"
    )

    db.session.add(category)
    db.session.commit()

    # Створення картини
    painting = Painting(
        name="Мона Ліза",
        artist="Да Вінчі",
        style="Ренесанс",
        year=1503,
        price=1000000,
        condition="Добрий",
        category_id=category.id,
        user_id=1
    )

    db.session.add(painting)
    db.session.commit()

    print("Painting created successfully")