from models.item import Item
from extensions import db

class ItemRepository:

    def get_all(self):
        return Item.query.all()

    def get_by_user(self, user_id):
        return Item.query.filter_by(user_id=user_id).all()

    def get_by_id(self, item_id):
        return db.session.get(Item, item_id)

    def add(self, item):
        db.session.add(item)
        db.session.commit()

    def delete(self, item):
        db.session.delete(item)
        db.session.commit()