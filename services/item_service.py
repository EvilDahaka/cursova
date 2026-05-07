from services.base_service import BaseService
from repositories.item_repository import ItemRepository
from models.item import Item
from dto.item_dto import ItemDTO
from extensions import db

class ItemService(BaseService):

    def __init__(self):
        super().__init__(ItemRepository())

    # Отримати всі товари користувача
    def get_by_user(self, user_id):
        return self.repository.get_by_user(user_id)

    # Отримати всі товари
    def get_all(self):
        return self.repository.get_all()

    # Отримати товар по id
    def get_by_id(self, item_id):
        return self.repository.get_by_id(item_id)

    # Створення нового товару
    def create(self, data, user_id):
        try:
            # DTO об'єкт
            dto = ItemDTO(
                name=data.get('name'),
                category_id=data.get('category_id'),
                year=data.get('year'),
                price=data.get('price'),
                condition=data.get('condition')
            )

            # Проста валідація
            if not dto.name:
                return False

            # Створення ORM об'єкта
            item = Item(
                name=dto.name,
                category_id=int(dto.category_id),
                year=int(dto.year),
                price=float(dto.price),
                condition=dto.condition,
                user_id=user_id
            )

            # Збереження через repository
            self.repository.add(item)

            return True

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    # Оновлення товару
    def update(self, item_id, data):
        try:
            item = self.repository.get_by_id(item_id)

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

    # Видалення товару
    def delete(self, item_id):
        try:
            item = self.repository.get_by_id(item_id)

            if item:
                self.repository.delete(item)
                return True

            return False

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    # Пошук товарів
    def search(self, query, user_id):

        if not query:
            return self.get_by_user(user_id)

        query = query.strip().lower()

        items = self.get_by_user(user_id)

        result = []

        for item in items:

            name = item.name.lower()

            category = (
                item.category.name.lower()
                if item.category else ""
            )

            if query in name or query in category:
                result.append(item)

        return result