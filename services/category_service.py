from models.category import Category
from extensions import db

class CategoryService:

    def get_all(self):
        return Category.query.all()

    def create(self, name):
        try:
            if not name:
                return False

            category = Category(name=name)
            db.session.add(category)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def delete(self, category_id):
        try:
            category = db.session.get(Category, category_id)
            if category:
                db.session.delete(category)
                db.session.commit()
                return True
            return False

        except Exception as e:
            db.session.rollback()
            print(e)
            return False