from extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Назва категорії
    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    # ORM зв'язок
    items = db.relationship(
        "Item",
        back_populates="category",
        cascade="all, delete-orphan"
    )

    # Представлення об'єкта
    def __repr__(self):
        return f"<Category {self.name}>"