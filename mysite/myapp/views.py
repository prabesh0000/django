from django.shortcuts import render , HttpResponse




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