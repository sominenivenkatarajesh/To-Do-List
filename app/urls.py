from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,CategoryCreateView, CategoryDeleteView


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("add/", TaskCreateView.as_view(), name="task-add"),
    path("edit/<int:pk>/", TaskUpdateView.as_view(), name="task-edit"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("category/add/", CategoryCreateView.as_view(), name="category-add"),
    path("category/delete/<int:pk>/", CategoryDeleteView.as_view(), name="category-delete"),
]
