from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

# Create your views here.

def login(response):
    pass

def technology(response):
    return render(response, "technology.html", {"visited": "technology"})

def news(response):
    return render(response, "news.html", {"visted": "news"})

def sports(response):
    return render(response, "sports.html", {"visted": "sports"})

def life(response):
    return render(response, "life.html", {"visted": "life"})