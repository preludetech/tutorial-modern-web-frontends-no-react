from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoItemForm
from .models import TodoItem


def home(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TodoItemForm()

    todos = TodoItem.objects.order_by("done", "id")
    return render(request, "todo/home.html", {"todos": todos, "form": form})


def toggle_todo_done(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.done = not todo.done
    todo.save()
    return render(request, "todo/partials/todo_item.html", {"item": todo})
