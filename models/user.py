from extensions import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    # ORM зв'язок
    items = db.relationship(
        "Item",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # Хешування пароля
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Перевірка пароля
    def check_password(self, password):
        return check_password_hash(
            self.password,
            password
        )

    # Представлення об'єкта
    def __repr__(self):
        return f"<User {self.username}>"