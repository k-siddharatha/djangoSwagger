from . import views
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
]
