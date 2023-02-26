from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .forms import DocumentForm
from .models import UploadedFile
# Create your views here.

def file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadedFile.objects.create()
            file = UploadedFile