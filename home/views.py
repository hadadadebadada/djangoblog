# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.

def homepage(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>HELLO WORLD</h1>")
    return render(request, "home.html", {})


def contacts(request, *args, **kwargs):
    # return HttpResponse("<h1>CONTACTS<h1>")
    return render(request, "contacts.html", {})


def bootstrap(request, *args, **kwargs):
    return render(request, "base.html", {})


def about(request, *args, **kwargs):
    mycontext = {"my_text": "this is my context",
                 "my_number": 123,
                 "my_list": [123, 123, 123, 123, "abc"],
                 "this_is_true": True}  ## python dictionary ##template variables
    return render(request, "about.html", mycontext)


def about(request, *args, **kwargs):
    mycontext = {"my_text": "this is my context",
                 "my_number": 123,
                 "my_list": [123, 123, 123, 123, "abc"],
                 "this_is_true": True}  ## python dictionary ##template variables
    return render(request, "about.html", mycontext)


def my_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.

    else:
        print()
