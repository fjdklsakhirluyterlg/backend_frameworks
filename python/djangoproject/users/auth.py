from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import UserCreationForm

def signup(request):

    if request.user.is_authenticated:

        return redirect("/")