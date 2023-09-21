from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    title = models.CharField(max_length=100, null=True, help_text="Your profession")
    
    bio = models.TextField(default="")
    date_of_birth = models.DateField(null=True)
    #height = models.FloatField(null=True)