from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def four_or_four_handler(request):
    request.status_code = 404