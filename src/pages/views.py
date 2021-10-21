from django.http import request
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contactpage_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def aboutpage_view(request, *args, **kwargs):
    return render(request, "about.html", {})