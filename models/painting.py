from extensions import db
from models.item import Item


class Painting(Item):
    __tablename__ = "paintings"

    id = db.Column(
        db.Integer,
        db.ForeignKey("items.id"),
        primary_key=True
    )

    # Автор картини
    artist = db.Column(
        db.String(100),
        nullable=True
    )

    # Стиль картини
    style = db.Column(
        db.String(100),
        nullable=True
    )

    __mapper_args__ = {
        "polymorphic_identity": "painting"
    }

    
    def get_extra_info(self):
        return f"Автор: {self.artist}"

    def __repr__(self):
        return f"<Painting {self.name}>"