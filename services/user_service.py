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
            user = User(username=username, is_admin=is_admin)
            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            print(f"[LOG] Created user {username}")

            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, id):
        try:
            user = User.query.get(id)
            if user:
                db.session.delete(user)
                db.session.commit()

                print(f"[LOG] Deleted user {id}")
                return True

            return False
        except Exception as e:
            print(e)
            return False