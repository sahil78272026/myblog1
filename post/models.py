from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
# this is the replica of Database of contact page
# makemigrations == create changes and store in a file
# migrate == apply the pending changes created by makemigrations in db
class Contact(models.Model): # like an excel sheet
    name = models.CharField(max_length=122) # like columns of an excel sheet , getting made in db
    email = models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    msg = models.TextField()
    date = models.DateField()

     # will show name in database objects
    def __str__(self):
        return "from : "  + self.name

class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(default=False) 
    slug = models.SlugField(default=False) 
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "from : "  + self.title

class CreateUserForm(UserCreationForm):
    class Meta:
        pass
    
   
