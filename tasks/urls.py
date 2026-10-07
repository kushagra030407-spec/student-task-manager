from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.task_create, name="task_create"),
    path("<int:pk>/edit/", views.task_update, name="task_update"),
    path("<int:pk>/toggle/", views.task_toggle, name="task_toggle"),
    path("<int:pk>/delete/", views.task_delete, name="task_delete"),
]
