from django.shortcuts import render, HttpResponse


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")
