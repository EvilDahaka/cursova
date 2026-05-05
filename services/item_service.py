from models.item import Item
from models.category import Category
from extensions import db
from sqlalchemy import func

class ItemService:

    def get_by_user(self, user_id):
        return Item.query.filter_by(user_id=user_id).all()

    def get_all(self):
        return Item.query.all()

    def get_by_id(self, item_id):
        return Item.query.get(item_id)

    def create(self, data, user_id):
        try:
            item = Item(
                name=data['name'],
                category_id=int(data['category_id']),
                year=int(data['year']),
                price=float(data['price']),
                condition=data['condition'],
                user_id=user_id
            )

            db.session.add(item)
            db.session.commit()

            print(f"[LOG] Created item {data['name']}")
            return True

        except Exception as e:
            print(e)
            return False

    def update(self, item_id, data):
        try:
            item = Item.query.get(item_id)
            if not item:
                return False

            item.name = data['name']
            item.category_id = int(data['category_id'])
            item.year = int(data['year'])
            item.price = float(data['price'])
            item.condition = data['condition']

            db.session.commit()
            return True

        except Exception as e:
            print(e)
            return False

    def delete(self, item_id):
        try:
            item = Item.query.get(item_id)
            if item:
                db.session.delete(item)
                db.session.commit()
                return True
            return False

        except Exception as e:
            print(e)
            return False


    def search(self, query, user_id):
        if not query:
            return self.get_by_user(user_id)

        query = query.strip().lower()

        items = self.get_by_user(user_id)

        result = []

        for item in items:
            name = item.name.lower() if item.name else ""
            category = item.category.name.lower() if item.category else ""

            if query in name or query in category:
                result.append(item)

        return result