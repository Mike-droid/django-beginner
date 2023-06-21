# from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.

def index(request):
  title = 'django course!!'
  return render(request, 'index.html', {
    'title': title
  })


def hello(request, username):
  return HttpResponse(f"<h1>Hello {username}</h1>")


def about(request):
  about_us = 'This is a great text'
  return render(request, 'about.html', {
    'about_us': about_us
  })


def projects(request):
  projects = list(Project.objects.values())
  return render(request, 'projects.html', {
    'projects': projects
  })


def tasks(request):
  # task = get_object_or_404(Task, id=id)
  return render(request, 'tasks.html')
