from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from .models import Posts, PostItem
from .forms import CreatePost

import validators


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


def add_post(response):
    print("response ", response.method)

    if response.method == "POST":
        errors = {}
        received_post = {
            "title": response.POST.get("post_title"),
            "text": response.POST.get("post_text"),
            "link": response.POST.get("post_link"),
            "image": response.POST.get("post_image"),
            "category": response.POST.get("post_category"),
        }

        print("\n\nrecursing\n\n")
        for key in received_post:
            if received_post[key].strip() == "":
                # if not key == "image":
                errors[key] = "Invalid"

        print("received: ", received_post)
        print(response.POST)
        print(response.POST.get("post_title"))

        print("the category ----->>>> ", received_post["category"])
        if not errors:
            print(errors)
            # post_category = received_post.category

            post = Posts.objects.get(name=received_post["category"])

            # creating PostItem
            post.postitem_set.create(
                title=received_post["title"],
                text=received_post["text"],
                image=received_post["image"],
                link=received_post["link"]
            ).save()

            # saving the PostItem

            form = CreatePost(response.POST)
            print("valid form: ", form.is_valid())

        # if form.is_valid():
        #     print("\n\n\ntitle is ", form.cleaned_data["title"])
        # else:
        #     print("\n\n\nIssue in form is valid")
    # else:

    return render(response, "add_post.html", {})
