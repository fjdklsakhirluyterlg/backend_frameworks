from django.shortcuts import render

# Create your views here.

def index(request):
    return render()

def add_todo(request):
    if request.method == "POST":
        request.data