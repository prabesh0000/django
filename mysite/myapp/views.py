from django.shortcuts import render , HttpResponse

from .models import*


def show_blog(request):
    blog = post.objects.all()
    context= {
        'blog':blog
    }
    return render(request, 'myapp/home.html',context)

# Create your views here.

def index(request):
    context = {
        'variable': "this is sent ",
        'variable2': "this is also sent "
    }
    return render (request, 'index.html' , context)
def about (request):
    return HttpResponse ("this is about  page")
def services (request):
    return HttpResponse ("this is serivices page")
def contact (request):
    return HttpResponse ("this is contact  page")