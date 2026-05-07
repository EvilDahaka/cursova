from datetime import datetime

from extensions import db


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)

    # Назва товару
    name = db.Column(
        db.String(100),
        nullable=False,
        index=True
    )

    # Категорія
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    # Рік
    year = db.Column(
        db.Integer,
        nullable=False
    )

    # Ціна
    price = db.Column(
        db.Float,
        nullable=False
    )

    # Стан
    condition = db.Column(
        db.String(50),
        nullable=False
    )

    # Користувач
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # Дата створення
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Дата оновлення
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # Поліморфізм
    type = db.Column(db.String(50))

    # ORM зв'язки
    category = db.relationship(
        "Category",
        back_populates="items"
    )

    user = db.relationship(
        "User",
        back_populates="items"
    )

    __mapper_args__ = {
        "polymorphic_identity": "item",
        "polymorphic_on": type
    }


    # Представлення об'єкта
    def __repr__(self):
        return f"<Item {self.name}>"
    
    def get_extra_info(self):
        return ""