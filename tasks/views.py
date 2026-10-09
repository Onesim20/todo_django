from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    ordering = ["-created_at"]


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_done = not task.is_done
        task.save()
    return redirect("task_detail", pk=task.pk)
