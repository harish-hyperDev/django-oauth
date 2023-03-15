from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from .models import Posts, PostItem


def login(response):
    pass


def technology(response):
    technology_posts = Posts.objects.get(name="Technology").postitem_set.all()
    return render(response, "technology.html", {"visited": "technology", "posts": technology_posts})


def news(response):
    news_posts = Posts.objects.get(name="News").postitem_set.all()
    return render(response, "news.html", {"visited": "news", "posts": news_posts})


def sports(response):
    sports_posts = Posts.objects.get(name="Sports").postitem_set.all()
    return render(response, "sports.html", {"visited": "sports", "posts": sports_posts})


def life(response):
    life_posts = Posts.objects.get(name="Life").postitem_set.all()
    return render(response, "life.html", {"visited": "life", "posts": life_posts})
