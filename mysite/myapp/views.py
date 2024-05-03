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
        #return redirect('/')
    task_list = Task.objects.all()
    return render(request, 'myapp/add.html', {'task_list': task_list})


def home (request):
    task_list = Task.objects.all()
    # for i in task_list:
    #     print(i.id)
    # print(task_list)
    return render(request, 'myapp/home.html', {'task_list': task_list})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    # print(id)
    return redirect('add')