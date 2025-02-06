from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, from Home Page!")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, from about Page!")

def contact(request):
    return HttpResponse("Hello, from contact Page!")