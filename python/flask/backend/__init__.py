from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    from .routes import routes

    app.register_blueprint(routes)

    return app