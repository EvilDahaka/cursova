from services.item_service import ItemService
from models.painting import Painting

class PaintingService(ItemService):

    def create_painting(self, data, user_id):

        painting = Painting(
            name=data.get("name"),
            artist=data.get("artist"),
            style=data.get("style"),
            category_id=data.get("category_id"),
            year=data.get("year"),
            price=data.get("price"),
            condition=data.get("condition"),
            user_id=user_id
        )

        self.repository.add(painting)

        return True