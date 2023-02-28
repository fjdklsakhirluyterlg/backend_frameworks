from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import UserCreationForm

def signup(request):

    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == ‘POST’:

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get(‘user’)

            password = form.cleaned_data.get(‘pass’)

            user = authenticate(username=user, password=pass)

            login(request, user)

            return redirect(‘/’)