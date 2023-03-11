from flask import Blueprint, request, redirect

auth = Blueprint("auth", __name__)

@auth.route("/auth/login")
def login():
    