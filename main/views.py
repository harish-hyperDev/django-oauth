from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.contrib.auth import authenticate, login    #for authenticating user login
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

from django.utils.safestring import mark_safe
from django.template import Library

from .models import Posts, PostItem
from .forms import CreatePost

import validators
import json


def login(response):
    if response.method == "GET":
        print("login")
        print(response.user)
        return render(response, "index.html", {})
    if response.method == "POST":
        print("login submit")
        username = response.POST["username"]
        password = response.POST["password"]
        print("user ", username, "pass ", password)
        user = authenticate(response, username=username, password=password)

        if user is not None:
            print("user is valid :D")
        else:
            print("user IS NOT valid!!")

    return render(response, "index.html", {})



def test(response):
    #all_posts = Posts.objects.get(name="Technology")
    #print(all_posts)

    print(response.user.is_authenticated)

    # verify_login_user = authenticate(username="harish2", password="aloha@123")
    #print("test user auth ", User.objects.get(username="test").is_authenticated())
    # login(verify_login_user)

    # print("user auth ", verify_login_user)

    '''
    if verify_login_user is None:
        print(verify_login_user)
        print("not authenticated")
    else:
        print(verify_login_user)
    '''

    return HttpResponse("<h1>Test</h1>")
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
            errors[key] = {}
            if received_post[key].strip() == "":
                errors[key] = "Invalid"

            if key == "link" or key == "image":
                if not validators.url(received_post[key]):
                    errors[key] = "Invalid"

        print("received: ", received_post)
        print(response.POST)
        print(response.POST.get("post_title"))
        print("\n\n")

        if not errors["title"] and not errors["text"] and not errors["link"] and not errors["image"]:
            print("no errors ", errors)
            # post_category = received_post.category

            if response.POST.get("submit") == "add":
                post = Posts.objects.get(name=received_post["category"])

                # creating PostItem
                post.postitem_set.create(
                    title=received_post["title"],
                    text=received_post["text"],
                    image=received_post["image"],
                    link=received_post["link"]
                ).save()

                # saving the PostItem

                # form = CreatePost(response.POST)
                # print("valid form: ", form.is_valid())
            elif json.loads(response.POST.get("submit"))["value"] == "edit":
                print("submit response ", json.loads(response.POST.get("submit")))

                post = Posts.objects.get(name=received_post["category"])
                postitem_id = json.loads(response.POST.get("submit"))["id"]

                edit_postitem = post.postitem_set.get(id=postitem_id)

                edit_postitem.title = received_post["title"]
                edit_postitem.text = received_post["text"]
                edit_postitem.link = received_post["link"]
                edit_postitem.image = received_post["image"]

                edit_postitem.save()

        else:
            print("errors ", errors)
            print("\n\n")
            print("received ", received_post)

            register = Library()
            @register.filter(is_safe=True)
            def js(obj):
                return mark_safe(json.dumps(obj))

            print("mark safe")
            print(js(received_post))

            data_dump = json.dumps(received_post)
            received_post["data_dump"] = data_dump
            return render(response, "add_post.html", {"errors": errors, "text_fields": js(received_post)})

    return render(response, "add_post.html", {"errors": {}})

def edit_post(response):
    edit_post = json.loads(response.POST.get("edit"))
    print("edit post ", edit_post)
    print("type ", type(edit_post))

    post = Posts.objects.get(name=edit_post["categoryName"]).postitem_set.get(id=edit_post["categoryId"])

    return post


def manage_post(response):
    post_categories = Posts.objects.all()

    print("\n\n-------Response : %s--------\n\n", response.method)
    if response.method == "POST":
        print("response -- ", response.method)

        if response.POST.get("edit"):
            post_model = edit_post(response)
            post = {
                "id": post_model.id,
                "title": post_model.title,
                "text": post_model.text,
                "link": post_model.link,
                "image": post_model.image,
                "category": str(post_model.category)
            }

            print("render post type " , type(post))
            print("category type: ", type(post["category"]))
            # print(post["link"])

            # print(rendered)

            # needs optimization
            register = Library()

            @register.filter(is_safe=True)
            def js(obj):
                return mark_safe(json.dumps(obj))

            print("mark safe")



            # new_post = serializers.serialize('json', PostItem.objects.all())
            # print(new_post)
            # print(js(post))
            # users = PostItem.objects.all()
            # print( JsonResponse({'data': list(users)}) )


            # data_dump = json.dumps(post)
            # post["data_dump"] = data_dump
            # print(post.id, post.text, post.title, post.category, post.link, post.image)

            # return render(response, "edit_post.html", json.loads({ "text_fields": {"title": post["title"], "text": post["text"], "link": post["link"], "image": post["image"], "id": post["id"], "category": post["category"]} }))
            return render(response, "edit_post.html", {"text_fields": js(post)})
            # print(response.POST.get("delete-confirm"))

        else:
            confirm_delete = json.loads(response.POST.get("delete-confirm"))
            print("confirm delete: ", confirm_delete)

            if confirm_delete:
                if confirm_delete["delete"] == "yes":
                    postitem_category = Posts.objects.get(name=confirm_delete["categoryName"])

                    delete_postitem = postitem_category.postitem_set.get(id=confirm_delete["categoryId"])
                    delete_postitem.delete()

            # delete_post.postitem_set.get(id=confirm_delete.categoryId).delete()

    all_posts = []
    for category in post_categories:
        items = category.postitem_set.all()
        for item in items:
            all_posts.append(item)

    # print("\n\n---all posts---\n\n", all_posts)
    # print("\n\nfirst post ", all_posts[0].text)
    return render(response, "manage_post.html", {"posts": all_posts})
