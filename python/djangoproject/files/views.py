from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import DocumentForm
from .models import UploadedFile
# Create your views here.

def index(request):
    return HttpResponse("Hello, World!")

def file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadedFile(request.FILES['filename'].name, request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/upload/success')
        else:
            return form.errors
    else:
        form = DocumentForm()
        return render(request, "upload.html", {"form":form})

def success(request):
    html = "<h1>Success!</h1>"
    return HttpResponse(html)