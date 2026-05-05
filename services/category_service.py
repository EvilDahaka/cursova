from models.category import Category
from extensions import db

class CategoryService:

    def get_all(self):
        return Category.query.all()

    def create(self, name):
        if not name or len(name.strip()) < 2:
            return False

        try:
            category = Category(name=name.strip())
            db.session.add(category)
            db.session.commit()

            print(f"[LOG] Category created: {name}")
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, category_id):
        try:
            category = Category.query.get(category_id)
            if category:
                db.session.delete(category)
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False