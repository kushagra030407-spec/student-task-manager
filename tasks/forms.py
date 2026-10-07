from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "priority"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Finish Python assignment", "autofocus": True}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Add a few details (optional)"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "priority": forms.Select(),
        }
        labels = {
            "title": "Task title",
            "description": "Description",
            "due_date": "Due date",
            "priority": "Priority",
        }
