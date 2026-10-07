from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task

def dashboard(request):
    tasks = Task.objects.all()
    status = request.GET.get("status", "all")
    query = request.GET.get("q", "").strip()

    if status == "pending":
        tasks = tasks.filter(completed=False)
    elif status == "completed":
        tasks = tasks.filter(completed=True)

    if query:
        tasks = tasks.filter(title__icontains=query) | tasks.filter(description__icontains=query)

    context = {
        "tasks": tasks.distinct(),
        "status": status,
        "query": query,
        "total_count": Task.objects.count(),
        "pending_count": Task.objects.filter(completed=False).count(),
        "completed_count": Task.objects.filter(completed=True).count(),
    }
    return render(request, "tasks/dashboard.html", context)

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'"{task.title}" was added.')
            return redirect("tasks:dashboard")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "page_title": "Add a task", "button_label": "Save task"})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Your task was updated.")
            return redirect("tasks:dashboard")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "page_title": "Edit task", "button_label": "Save changes"})

@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    messages.success(request, "Task marked as completed." if task.completed else "Task moved back to pending.")
    return redirect(request.META.get("HTTP_REFERER") or "tasks:dashboard")

@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    title = task.title
    task.delete()
    messages.success(request, f'"{title}" was deleted.')
    return redirect("tasks:dashboard")
