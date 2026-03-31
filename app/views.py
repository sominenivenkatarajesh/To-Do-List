from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Category



class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context["categories"] = Category.objects.all()
        context["total_count"] = tasks.count()
        context["completed_count"] = tasks.filter(completed=True).count()
        context["pending_count"] = tasks.filter(completed=False).count()
        return context


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task-list")



class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]
    template_name = "category_form.html"
    success_url = reverse_lazy("task-list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task-list")
