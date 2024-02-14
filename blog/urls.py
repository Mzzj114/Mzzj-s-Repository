from django.shortcuts import redirect
from django.urls import path, reverse
from . import views

app_name = "blog"
urlpatterns = [
    path("index", views.index, name="index"),
    path("posts/<str:posttitle>", views.posts, name="posts"),
    path("index/search", views.search, name="search"),
    path("", lambda request: redirect(reverse('index'))),
]