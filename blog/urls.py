from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("index", views.index, name="index"),
    path("posts/<str:posttitle>", views.posts, name="posts"),
    path("", views.index)
]