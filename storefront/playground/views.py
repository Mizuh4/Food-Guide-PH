from django.http import HttpResponse
from django.shortcuts import render

'''
request handler, action, view function
pull data from db, transform data, and send email
return HttpResponse('Hello World')
'''

def index(request):
    return render(request, "hello/index.html")

def greet_name(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })