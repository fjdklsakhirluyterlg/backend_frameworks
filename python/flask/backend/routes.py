from flask import Blueprint
from .models import Todo

routes = Blueprint(__name__, "routes")

@routes.route("/")
def index():
    return "hi"

