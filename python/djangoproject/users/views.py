from django.shortcuts import render

# Create your views here.

def handle_avataer_upload(FILE):
    pass

def upload_avatar(request):
    if request.method == "POST":
        files = request.FILES
        handle_avataer_upload(files)