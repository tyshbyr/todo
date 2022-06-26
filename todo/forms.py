from django import forms
from tempus_dominus.widgets import DateTimePicker

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status']
        widgets = {
            'deadline': DateTimePicker(attrs={'append': 'fa fa-calendar'}),
            'status': forms.Select(attrs={'class': "btn btn-secondary dropdown-toggle"})
        }
