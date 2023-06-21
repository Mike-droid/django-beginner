from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import CreateNewTask

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
  tasks = Task.objects.all()
  return render(request, 'tasks.html', {
    'tasks': tasks
  })


def create_task(request):
  if request.method == 'GET':
    return render(request, 'create_task.html', {
      'form': CreateNewTask()
    })
  else:
    Task.objects.create(
      title=request.POST['title'],
      description=request.POST['description'],
      project_id=2
    )
    return redirect('/tasks/') #! El '/' al inicio es requerido
