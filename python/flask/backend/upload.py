from pathlib import Path
from flask import Blueprint, request

upload = Blueprint(__name__, "upload")

UPLOAD_FOLDER = Path(Path.cwd())

@upload.route("/upload")
def upload_file():
    if request.method == "POST":
        files = request.files
        