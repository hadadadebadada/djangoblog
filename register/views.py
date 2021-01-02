from django.shortcuts import render, redirect
from register import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def homepage(request, *args, **kwargs):  ## cumstom imput
    form = forms.AddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = forms.AddressForm()

    return render(request, "register.html", {"form": form})


def register(request):  ## django build in input(user creation form)
    form = forms.RegisterForm()
    ##saving user to database
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user + " you are now able to login")
            return redirect('login')

    return render(request, "accounts/register.html", {"form": form})
