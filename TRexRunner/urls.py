from django.urls import path, include
from . import views

app_name = "TRexRunner"
urlpatterns = [
    path('', views.t_rex_runner),
]
