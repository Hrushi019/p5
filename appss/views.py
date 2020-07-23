from django.shortcuts import render
from django.http import HttpResponse
from math import factorial
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to views of an APP</h1>")

def home(request):
    return render(request,"appss/home.html",{'name':"Hrushikesh"})

def facto(request,n):
    n = int(n)
    return HttpResponse("Factorial is {}".format(factorial(n)))
