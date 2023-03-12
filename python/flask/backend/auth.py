from flask import Blueprint, request, redirect
from .models import User

auth = Blueprint("auth", __name__)

@auth.route("/auth/login")
def login():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        password = data["password"]
