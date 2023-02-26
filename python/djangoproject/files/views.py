from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
# Create your views here.

def file(request):
    if request.method == "POST":
        request.files