from django.contrib import admin
from .models import *
from .models import catagory

# Register your models here.


admin.site.register(post)
admin.site.register(catagory)