from extensions import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    year = db.Column(db.Integer)
    price = db.Column(db.Float)
    condition = db.Column(db.String(50))
    user_id = db.Column(db.Integer)

    category = db.relationship("Category")