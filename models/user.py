class User:
    """
    Базовий клас користувача
    """

    def __init__(self, id, username, is_admin):
        self.id = id
        self.username = username
        self.is_admin = is_admin

    def is_admin_user(self):
        return self.is_admin


class AdminUser(User):
    """
    Адміністратор (успадкування)
    """

    def __init__(self, id, username):
        super().__init__(id, username, True)