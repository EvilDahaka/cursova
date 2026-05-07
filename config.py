class Config:

    # Секретний ключ Flask
    SECRET_KEY = "secret"

    # SQLite база даних
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

    # Вимикаємо зайві попередження
    SQLALCHEMY_TRACK_MODIFICATIONS = False