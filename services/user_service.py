from models.user import User
from extensions import db

class UserService:

    def login(self, username, password):
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            return user

        return None

    def get_all(self):
        return User.query.all()

    def create(self, username, password, is_admin):
        try:
            if not username or not password:
                return False

            user = User(username=username, is_admin=is_admin)
            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            return True

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def delete(self, id):
        try:
            user = db.session.get(User, id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return True
            return False

        except Exception as e:
            db.session.rollback()
            print(e)
            return False