from pathlib import Path
from flask import Blueprint, request

upload = Blueprint(__name__, "upload")

UPLOAD_FOLDER = Path(Path.cwd() / "files")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload.route("/upload")
def upload_file():
    if request.method == "POST":
        files = request.files

        