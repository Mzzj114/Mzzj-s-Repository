from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:language>/', views.index, name="index"),
    path('<str:language>/video/', views.thingsPage, name="videoPage"),
    path('<str:language>/community/', views.commuPage, name="commuPage"),
]

