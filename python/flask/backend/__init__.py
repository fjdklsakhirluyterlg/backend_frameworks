from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .routes import routes

    app.register_blueprint(routes)


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    return app