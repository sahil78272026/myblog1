from django.urls import path
from post import views
from django.contrib import admin

urlpatterns = [
    path('',views.home,name='home'),
 ]
