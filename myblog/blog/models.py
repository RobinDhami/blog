from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

class Profile(models.Model):
    image = models.ImageField()
    bio = models.TextField()
    location = models.CharField(max_length=200,blank=True,null=True)