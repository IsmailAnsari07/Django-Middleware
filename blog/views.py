from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    print('This will be in Views')
    return HttpResponse("this is a Home page.!")
    
