from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def signup(request: HttpRequest):
    return render(request, 'signup.html')

def login(request: HttpRequest):
    return render(request, 'login.html')