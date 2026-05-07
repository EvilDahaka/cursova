from models.user import User
from extensions import db

class UserRepository:

    def get_all(self):
        return User.query.all()

    def get_by_id(self, user_id):
        return db.session.get(User, user_id)

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def add(self, user):
        db.session.add(user)
        db.session.commit()

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()