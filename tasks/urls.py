from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("delete-all/", views.delete_all_task, name="delete_all_task"),
    path("edit/<int:task_id>", views.edit_task, name="edit_task"),
]
