from django.db import models
from django.db.models import Model
class User(models.Model):
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
