from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Recipe

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    return HttpResponseRedirect(reverse("recipes:home"))
    
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    return render(request, "recipes/home.html", {
        "regions": Recipe.REGIONS.values()
    })

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    return render(request, "recipes/profile.html", {
        "name": request.user.username
    })

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("recipes:index"))
        else:
            return render(request, "recipes/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "recipes/login.html")

def logout_view(request):
    logout(request)
    return render(request, "recipes/login.html", {
        "message": "Successfully Logged Out"
    })

def signup_view(request):
    pass
    #return HttpResponse("Signup View")