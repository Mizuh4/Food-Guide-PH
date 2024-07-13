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
            "section": "authentic",
            "name": request.user.username,
            "regions": Recipe.REGIONS.values()
    })

def section(request, section):
    print("from section function: " + section)
    print(type(section))
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    
    if section:
        content = render(request, f"recipes/{section}.html", {
            "section": "authentic",
            "name": request.user.username,
            "regions": Recipe.REGIONS.values()
        })
        print(type(content))
        return content

    else:
        raise Http404("No such section.")

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