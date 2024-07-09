from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "recipes/index.html", {
        
    })

def login_view(request):
    return render(request, "recipes/login.html", {
        
    })

def logout_view(request):
    return render(request, "recipes/logout.html", {
        
    })

def signup_view(request):
    return HttpResponse("Signup View")