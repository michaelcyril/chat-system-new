from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USERNAME_FIELD = 'username'

class Profile(models.Model):
    gender_choice = (("Male", "male"), ("Female", "female"),)
    phone=models.CharField(max_length=14)
    bio=models.TextField()
    instagram=models.URLField(max_length=200)
    linkedin=models.URLField(max_length=200)
    twitter=models.URLField(max_length=200)
    feature_image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    gender=models.CharField(max_length=20,choices=gender_choice,default='1')