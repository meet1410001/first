from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('registration', views.registration),
    path('index', views.index),
]