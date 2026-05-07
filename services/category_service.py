from services.base_service import BaseService
from repositories.category_repository import CategoryRepository
from models.category import Category
from extensions import db

class CategoryService(BaseService):

    def __init__(self):
        super().__init__(CategoryRepository())

    def get_all(self):
        return self.repository.get_all()

    def create(self, name):
        try:
            if not name:
                return False

            category = Category(name=name)

            self.repository.add(category)
            return True

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def delete(self, category_id):
        try:
            category = self.repository.get_by_id(category_id)

            if category:
                self.repository.delete(category)
                return True

            return False

        except Exception as e:
            db.session.rollback()
            print(e)
            return False