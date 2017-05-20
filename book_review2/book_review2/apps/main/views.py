from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "main/index.html")

def home(request):
    return render(request, "main/home.html")

def success(request):
    return render(request, 'main/success.html')
