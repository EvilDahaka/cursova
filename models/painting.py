from extensions import db
from models.item import Item

class Painting(Item):
    __tablename__ = "paintings"

    id = db.Column(db.Integer, db.ForeignKey("items.id"), primary_key=True)

    artist = db.Column(db.String(100), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "painting"
    }