from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'

    from .routes import routes

    app.register_blueprint(routes)

    db.init_app(app)

    return app