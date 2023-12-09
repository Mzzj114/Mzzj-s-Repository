from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:language>/', views.index, name="index"),
    path('<str:language>/video/', views.videoPage, name="videoPage"),
    path('<str:language>/community/', views.commuPage, name="commuPage"),
]

# 加一个可变的char作为语言判断