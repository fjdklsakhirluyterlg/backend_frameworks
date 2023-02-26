from pathlib import Path
from flask import Blueprint, request

upload = Blueprint(__name__, "upload")

@upload.route("/upload")
def upload_file():
    if request.method == "POST":
        files = request.files
        