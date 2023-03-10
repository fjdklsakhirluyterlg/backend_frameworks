from django.shortcuts import render
from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    return render()

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            instance = Todo(title)
            instance.save()
    else:
        return render()

def show_todo(request):
    all_todo = Todo.objects.all()