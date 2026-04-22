from flask import Flask

app = Flask(__name__)
app.secret_key = "secret123"

from routes.item_routes import item_bp
from routes.auth_routes import auth_bp

app.register_blueprint(item_bp)
app.register_blueprint(auth_bp)