from django.shortcuts import render , HttpResponse




# Create your views here.

def index(request):
    context = {
        'variable': "this is sent ",
        'variable2': "this is also sent "
    }
    return render (request, 'index.html' , context)
def about (request):
    return render  (request, 'about.html')
    # return HttpResponse ("hello")
def services (request):
    return render ( request, 'services.html')
def contact (request):
    return render( request , 'contact')