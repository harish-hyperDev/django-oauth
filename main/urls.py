from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('main.urls')),
    #path('', TemplateView.as_view(template_name="index.html")),

    path('', views.login_user, name="login"),
    path('technology/', views.technology, name="technology"),
    path('news/', views.news, name="news"),
    path('sports/', views.sports, name="sports"),
    path('life/', views.life, name="life"),
    path('add/', views.add_post, name="add_post"),
    path('edit/', views.edit_post, name="edit_post"),
    path('manage/', views.manage_post, name="manage_post"),
    path('test/', views.test, name="test"),
    # path('accounts/google/login/', TemplateView.as_view(template_name="oauth_signin.html")),
    # path('accounts/', include('allauth.urls')),
    # path('logout/', LogoutView.as_view()),
]


# path('', TemplateView.as_view(template_name="index.html")),