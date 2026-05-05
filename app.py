from flask import Flask
from extensions import db  

from routes.item_routes import item_bp
from routes.auth_routes import auth_bp
from routes.category_routes import category_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.secret_key = 'secret'

#SQLAlchemy конфіг
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#ініціалізація ORM
db.init_app(app)

#РЕЄСТРАЦІЯ ROUTES
app.register_blueprint(item_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(category_bp)
app.register_blueprint(user_bp)


#створення таблиць 
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)