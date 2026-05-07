from flask import Flask

from config import Config
from extensions import db

from routes.item_routes import item_bp
from routes.auth_routes import auth_bp
from routes.category_routes import category_bp
from routes.user_routes import user_bp
from models.painting import Painting
from models.coin import Coin

app = Flask(__name__)

# Завантаження конфігурації
app.config.from_object(Config)

# Ініціалізація SQLAlchemy
db.init_app(app)

# Реєстрація blueprint
app.register_blueprint(item_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(category_bp)
app.register_blueprint(user_bp)

# Створення таблиць
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)