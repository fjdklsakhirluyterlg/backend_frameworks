from quart import Quart
from quart_sqlalchemy import Sqlalchemy


db = Sqlalchemy()

def create_app():
    app = Quart(__name__)

    return app