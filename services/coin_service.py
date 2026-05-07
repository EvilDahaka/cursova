from services.item_service import ItemService
from models.coin import Coin

class CoinService(ItemService):

    def create_coin(self, data, user_id):

        coin = Coin(
            name=data.get("name"),
            material=data.get("material"),
            country=data.get("country"),
            nominal=data.get("nominal"),
            category_id=data.get("category_id"),
            year=data.get("year"),
            price=data.get("price"),
            condition=data.get("condition"),
            user_id=user_id
        )

        self.repository.add(coin)

        return True