from django.shortcuts import redirect, render

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

    todos = TodoItem.objects.all()
    return render(request, "todo/home.html", {"todos": todos, "form": form})


# def toggle_done(request):
