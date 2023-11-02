from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class User(AbstractUser):
    choice_gender = ((0, "Nu"),(1, "Nam"),(2, "Khong Xac Dinh"))
    age  = models.IntegerField(default=0)
    gender = models.IntegerField(choices= choice_gender, default=0)
    address = models.CharField(default=' ', max_length=255)

