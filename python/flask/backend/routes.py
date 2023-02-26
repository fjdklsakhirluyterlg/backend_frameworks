from flask import Blueprint

routes = Blueprint(__name__, "routes")

@routes.route("/")
def index():
    return "hi"