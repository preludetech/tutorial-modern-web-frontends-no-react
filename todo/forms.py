from django import forms

from .models import TodoItem


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["title", "description"]
        widgets = {"description": forms.Textarea(attrs={"rows": 2})}
