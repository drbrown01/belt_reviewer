from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "main/index.html")

def home(request):
    return render(request, "main/home.html")

def success(request):
    return render(request, 'main/success.html')

def reviews(request):
    return render(request, 'main/reviews.html')

def account(request):
    return render(request, 'main/account.html')

def logout(request):
    return render(request, 'main/logout.html')
