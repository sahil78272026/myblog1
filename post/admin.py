import imp
from django import views
from django.contrib import admin
from .models import Contact, Post
# Register your models here.

admin.site.register(Contact)
admin.site.register(Post)
