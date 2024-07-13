from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from django.shortcuts import render
from django.urls import reverse
from .models import Recipe

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    return render(request, "recipes/home.html", {
            "display": "authentic",
            "name": request.user.username,
            "regions": Recipe.REGIONS.values()
    })

def display(request, display):
    print("from display function: " + display)
    print(type(display))
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    
    if display:
        content = render(request, f"recipes/{display}.html", {
            "display": "authentic",
            "name": request.user.username,
            "regions": Recipe.REGIONS.values()
        })
        print(type(content))
        return content

    else:
        raise Http404("No such display")

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