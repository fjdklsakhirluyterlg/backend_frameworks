from django.shortcuts import render

# Create your views here.

def upload_avatar(request):
    if request.method == "POST":
        