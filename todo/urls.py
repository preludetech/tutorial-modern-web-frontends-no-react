from django.urls import path

from todo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo/<int:pk>/toggle/", views.toggle_todo_done, name="toggle_todo_done"),
    # path("partials/todo_list", views.partial_todo_list, name="partial_todo_list"),
]
