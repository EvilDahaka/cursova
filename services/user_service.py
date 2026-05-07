from services.base_service import BaseService
from repositories.user_repository import UserRepository
from models.user import User
from extensions import db

class UserService(BaseService):

    def __init__(self):
        super().__init__(UserRepository())

    def login(self, username, password):
        user = self.repository.get_by_username(username)

        if user and user.check_password(password):
            return user

        return None

    def get_all(self):
        return self.repository.get_all()

    def create(self, username, password, is_admin):
        try:
            if not username or not password:
                return False

            user = User(
                username=username,
                is_admin=is_admin
            )

            user.set_password(password)

            self.repository.add(user)
            return True

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def delete(self, user_id):
        try:
            user = self.repository.get_by_id(user_id)

            if user:
                self.repository.delete(user)
                return True

            return False

        except Exception as e:
            db.session.rollback()
            print(e)
            return False