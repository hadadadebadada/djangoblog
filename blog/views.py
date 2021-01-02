from django.shortcuts import render

from django.shortcuts import render

# Create your views here.   ## cumstom homepage erstellung hier
from .models import BlogEntry  ##product class muss importiert werden also models.py in products
from django.shortcuts import render
from django.http import HttpResponse
from blog import forms


# Create your views here.
def product_create_view(request):  ##weg1
    form = forms.ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = forms.ProductForm()
    context = {"form": form}
    return render(request, "blog/blogentry.html", context)


def product_detail_view(request):
    obj = BlogEntry.objects.get(id=1)  ## Looping trough all database blog entrys

    context = {
        #  'title': obj.title,
        #        'description:': obj.description
        'object': obj

    }

    return render(request, "blog/detail.html", context)


def index(request):
    queryset = BlogEntry.objects.all()
    context = {'allObjects': queryset}
    return render(request, "blog/detail.html", context)


def product_create_view(request):  ##weg2 (besser)
    my_form = forms.RawProductForm()
    if request.method == "POST":
        my_form = forms.RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            BlogEntry.objects.create(**my_form.cleaned_data)  ##** verwandenln in attribute
        else:
            print(my_form.errors)
    context = {"form": my_form}

    return render(request, "blog/blogentry.html", context)
