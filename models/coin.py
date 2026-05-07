from extensions import db
from models.item import Item

class Coin(Item):
    __tablename__ = "coins"

    id = db.Column(db.Integer, db.ForeignKey("items.id"), primary_key=True)

    material = db.Column(db.String(50), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "coin"
    }