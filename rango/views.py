from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there parther!")

def about(request):
    return HttpResponse("rango says here is about page")