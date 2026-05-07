from extensions import db
from models.item import Item


class Coin(Item):
    __tablename__ = "coins"

    id = db.Column(
        db.Integer,
        db.ForeignKey("items.id"),
        primary_key=True
    )

    # Матеріал монети
    material = db.Column(
        db.String(50),
        nullable=True
    )

    # Країна
    country = db.Column(
        db.String(100),
        nullable=True
    )

    __mapper_args__ = {
        "polymorphic_identity": "coin"
    }

    
    def get_extra_info(self):
        return f"Матеріал: {self.material}"

    def __repr__(self):
        return f"<Coin {self.name}>"