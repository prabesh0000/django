from django.contrib import admin
from django.urls import path , include
from myapp import views

urlpatterns = [
 path ('', views.index ,  name = 'myapp'),
 path ('services', views.services ,  name = 'myapp'),
 path ('about', views.about ,  name = 'about'),
 path ('contact', views.about ,  name = 'about')
]
