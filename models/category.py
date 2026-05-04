class Category:
    """
    Модель категорії (об'єкт предметної області)
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name