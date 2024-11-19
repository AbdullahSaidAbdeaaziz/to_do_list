from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import TaskForm
from .models import Task


# Create your views here.
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title, user=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("index")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("index")


def delete_all_task(request):
    if request.method == "POST":
        tasks = Task.objects.all()
        tasks.delete()
        return redirect("index")
    else:
        return HttpResponseNotAllowed(["POST"])


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit_task.html", {"form": form, "task": task})
