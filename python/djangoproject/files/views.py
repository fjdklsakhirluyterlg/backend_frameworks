from django.shortcuts import render

# Create your views here.

def file(request):
    if request.method == "POST":
        request.files