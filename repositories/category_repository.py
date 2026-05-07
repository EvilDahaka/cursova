from models.category import Category
from extensions import db

class CategoryRepository:

    def get_all(self):
        return Category.query.all()

    def get_by_id(self, category_id):
        return db.session.get(Category, category_id)

    def add(self, category):
        db.session.add(category)
        db.session.commit()

    def delete(self, category):
        db.session.delete(category)
        db.session.commit()