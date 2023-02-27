from flask import Blueprint, request
from .models import Todo
from . import db

routes = Blueprint(__name__, "routes")

@routes.route("/")
def index():
    return "hi"

@routes.route("/api/todo/add")
def add_todo():
    data = request.get_json()
    title = data["title"]
    new = Todo(title=title)
    db.session.add(new)
