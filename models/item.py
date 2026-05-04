class Item:
    """
    Модель антикварного товару (об'єкт предметної області)
    """

    def __init__(
        self,
        id,
        name,
        category_id,
        year,
        price,
        condition,
        user_id,
        category_name=None
    ):
        # Основні поля товару
        self.id = id
        self.name = name
        self.category_id = category_id
        self.year = year
        self.price = price
        self.condition = condition
        self.user_id = user_id

        # Назва категорії (з JOIN)
        self.category_name = category_name

    def __str__(self):
        # Зручне текстове представлення
        return f"{self.name} ({self.year})"