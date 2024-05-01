from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def add(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        priority = request.POST.get("priority", "")
        description = request.POST.get("description", "")
        status = request.POST.get("status", "")
        date = request.POST.get("date", "")
        task = Task(name=name, priority=priority, description=description, status=status,  date=date)
        task.save()
        return redirect('/')
    return render(request, 'myapp/add.html')


def home (request):
    task_list = Task.objects.all()
    return render(request, 'myapp/home.html', {'task_list': task_list})