from django.shortcuts import render, redirect
from register import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login(request, *args, **kwargs):  ## cumstom imput

    if request.method == "POST":
        request.POST.get("username")
        request.POST.get("password")

        user = authenticate(request,username = forms.get("username"),password = forms.get("password"))
        if user is not None:
            login(request, user)
    context = {}
    return render(request, "accounts/login.html", context)


