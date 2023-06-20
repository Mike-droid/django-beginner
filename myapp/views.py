# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Index Page")


def hello(request, username):
  return HttpResponse(f"<h1>Hello {username}</h1>")


def about(request):
  return HttpResponse("<p>About</p>")

