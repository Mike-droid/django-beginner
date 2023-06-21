# from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'index.html')


def hello(request, username):
  return HttpResponse(f"<h1>Hello {username}</h1>")


def about(request):
  return render(request, 'about.html')


def projects(request):
  projects = list(Project.objects.values())
  return render(request, 'projects.html')


def tasks(request):
  # task = get_object_or_404(Task, id=id)
  return render(request, 'tasks.html')
