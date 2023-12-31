from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

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
  return render(request, 'projects/projects.html', {
    'projects': projects
  })


def create_project(request):
  if request.method == 'GET':
    return render(request, 'projects/create_project.html', {
      'form': CreateNewProject()
    })
  else:
    Project.objects.create(name=request.POST['name'])
    return redirect('projects')


def project_detail(request, id):
  project = get_object_or_404(Project, id=id)
  tasks = Task.objects.filter(project_id = id)
  return render(request, 'projects/project_detail.html', {
    'project': project,
    'tasks': tasks
  })


def tasks(request):
  # task = get_object_or_404(Task, id=id)
  tasks = Task.objects.all()
  return render(request, 'tasks/tasks.html', {
    'tasks': tasks
  })


def create_task(request):
  if request.method == 'GET':
    return render(request, 'tasks/create_task.html', {
      'form': CreateNewTask()
    })
  else:
    Task.objects.create(
      title=request.POST['title'],
      description=request.POST['description'],
      project_id=2
    )
    return redirect('tasks')
