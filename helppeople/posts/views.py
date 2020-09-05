from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def posts(request):
    return HttpResponse('<h1>Posts Home</h1>')

def about(request):
    return HttpResponse('<h1>Posts About</h1>')