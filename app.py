from flask import Flask
from routes.item_routes import item_bp
from routes.auth_routes import auth_bp
from routes.category_routes import category_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.secret_key = 'secret'

app.register_blueprint(item_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(category_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)