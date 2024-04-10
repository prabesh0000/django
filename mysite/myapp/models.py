from typing import Any
from django.db import models

# Create your models here.

class catagory(models.Model):
    catagory_name=models.CharField( max_length=250)

    def __str__(self):
       return self.catagory_name

class post(models.Model) :
    title = models.CharField(max_length= 250)
    body = models.TextField()
    category = models.ForeignKey(catagory,on_delete=models.CASCADE)