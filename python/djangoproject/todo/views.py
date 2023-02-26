from django.shortcuts import render
from .forms import TodoForm

# Create your views here.

def index(request):
    return render()

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            