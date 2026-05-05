from extensions import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    condition = db.Column(db.String(50), nullable=False)

    # 🔥 FOREIGN KEY
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    category = db.relationship("Category")