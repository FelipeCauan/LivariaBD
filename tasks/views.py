from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')

    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    return render(request, 'tasks/list.html', {'tasks': tasks})


def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

# Create your views here.
