from flask import Blueprint, request, redirect
from .models import User
from flask_login import login_user

auth = Blueprint("auth", __name__)

@auth.route("/auth/login")
def login():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        user = User.query.filter_by(name=name).first()
        password = data["password"]
        if user.password == password:
            login_user(user)

@auth.route("/auth/signup")
def signup():
    if request.methd == "POST":
        data = request.get_json()

