from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from django.shortcuts import render
from django.urls import reverse
from .models import Recipe

# Create your views here.
sections = ["authentic", "signature", "profile", "cookbooks", "settings"]


def index(request, section):
    global sections
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    
    if section in sections:
        return render(request, "recipes/home.html", {
                "section": section,
                "name": request.user.username,
                "regions": Recipe.REGIONS.values()
        })
    else:
        return index_blank(request)

def index_blank(request):
    return index(request, "authentic")

def section(request, section):
    global sections
    print("from section function: " + section)
    print(type(section))

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    
    if section in sections:
        return render(request, f"recipes/sections/{section}.html", {
            "section": section,
            "name": request.user.username,
            "regions": Recipe.REGIONS.values()
        })
        print(type(content))

    else:
        raise Http404("Web Page does not exist.")

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("recipes:index_blank"))
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