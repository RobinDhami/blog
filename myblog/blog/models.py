from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

class Blogger(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True)
    bio = models.TextField()
    location = models.CharField(max_length=200,blank=True,null=True)