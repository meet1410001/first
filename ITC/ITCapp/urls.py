from django.contrib import admin
from django.urls import path
from . import views
"""
urlpatterns = [
    path('', views.login),
    #path('registration', views.registration),
]
"""

urlpatterns = [
    path('', views.login, name='login'),  # Add this line
    path('registration', views.registration, name='registration'),
    #path('register', views.register, name='register'),
]
