from django.shortcuts import render
from django.template import RequestContext
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
            instance = UploadedFile.objects.create()
            instance.myfile.save(request.FILES['filename'].name, request.FILES['file'])
            instance.save()
            return HttpResponse("saved")
        else:
            return form.errors
    else:
        form = DocumentForm()
        return render(request, "upload.html", {"form":form})