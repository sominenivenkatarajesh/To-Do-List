from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    CategoryCreateView, CategoryDeleteView, RegisterView
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("add/", TaskCreateView.as_view(), name="task-add"),
    path("edit/<int:pk>/", TaskUpdateView.as_view(), name="task-edit"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("category/add/", CategoryCreateView.as_view(), name="category-add"),
    path("category/delete/<int:pk>/", CategoryDeleteView.as_view(), name="category-delete"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
