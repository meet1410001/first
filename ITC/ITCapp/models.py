from django.db import models
from django.db.models import Model

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)  # Increased the max length
    email = models.EmailField()
    age = models.IntegerField()
    city = models.CharField(max_length=50)  # Increased the max length
    state = models.CharField(max_length=50)  # Increased the max length
    country = models.CharField(max_length=50)  # Increased the max length