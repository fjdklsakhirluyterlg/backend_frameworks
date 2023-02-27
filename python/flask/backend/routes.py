from flask import Blueprint, request
from .models import Todo

routes = Blueprint(__name__, "routes")

@routes.route("/")
def index():
    return "hi"

@routes.route("/api/todo/add")
def add_todo():
    data = request.get_json()
