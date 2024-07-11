from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Recipe

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))
    display = "authentic"   
    return HttpResponseRedirect(reverse("recipes:home", args=(display,)))


def home(request, display):
    print(display)
    print(type(display))
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("recipes:login"))

    if display == "authentic":
        return render(request, "recipes/section.html", {
            "display": "authentic",
            "name": request.user.username,
            "regions": Recipe.REGIONS.values()
        })
    
    elif display == "signature":
        return render(request, "recipes/section.html", {
            "display": "signature",
            "name": request.user.username,
            "regions": Recipe.REGIONS.values()
        })
    
    else:
        raise Http404("LOLOLOL")

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