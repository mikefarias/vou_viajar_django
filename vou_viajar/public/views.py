from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'public/index.html')

def login(request):
    return render(request, 'conta/login.html')

def logout(request):
    index(request)

def destinos(request):
    return render(request, 'public/places.html')

def blog(request):
    return render(request, 'public/blog.html')



