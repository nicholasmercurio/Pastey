from django.db import models

# Create your models here.
class User(models.Model):
    name        = models.CharField(max_length=100)
    email       = models.TextField(max_length=120)
    password    = models.TextField(max_length=120)
