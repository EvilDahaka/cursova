from models.item import Item
from models.category import Category
from extensions import db

class ItemService:

    def get_by_user(self, user_id):
        return Item.query.filter_by(user_id=user_id).all()

    def get_all(self):
        return Item.query.all()

    def get_by_id(self, item_id):
        return db.session.get(Item, item_id)

    def create(self, data, user_id):
        try:
            name = data.get('name')
            category_id = data.get('category_id')
            year = data.get('year')
            price = data.get('price')
            condition = data.get('condition')

            if not name or not category_id:
                return False

            # проста валідація стану
            if condition not in ["Новий", "Вживаний", "На запчастини"]:
                return False

            item = Item(
                name=name,
                category_id=int(category_id),
                year=int(year),
                price=float(price),
                condition=condition,
                user_id=user_id
            )

            db.session.add(item)
            db.session.commit()

            return True

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def update(self, item_id, data):
        try:
            item = db.session.get(Item, item_id)
            if not item:
                return False

            item.name = data.get('name')
            item.category_id = int(data.get('category_id'))
            item.year = int(data.get('year'))
            item.price = float(data.get('price'))
            item.condition = data.get('condition')

            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def delete(self, item_id):
        try:
            item = db.session.get(Item, item_id)
            if item:
                db.session.delete(item)
                db.session.commit()
                return True
            return False

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def search(self, query, user_id):
        if not query:
            return self.get_by_user(user_id)

        query = query.strip().lower()

        items = self.get_by_user(user_id)

        result = []
        for item in items:
            name = item.name.lower()
            category = item.category.name.lower() if item.category else ""

            if query in name or query in category:
                result.append(item)

        return result