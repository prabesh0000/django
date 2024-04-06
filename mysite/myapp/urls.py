from django.contrib import admin
from django.urls import path , include
from mysite import views

urlpatterns = [
    path("", views.index ,  name= 'project')

]