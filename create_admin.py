from app import app
from extensions import db
from models.user import User

with app.app_context():
    user = User(username="admin", is_admin=True)
    user.set_password("1234")

    db.session.add(user)
    db.session.commit()

    print("Admin created!")