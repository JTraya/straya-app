from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello from Straya!<h1>')

def about(request):
    return HttpResponse('<h1>About Straya<h1>')