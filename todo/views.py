from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm


class TaskMixinView(LoginRequiredMixin):
    def get_queryset(self):
            return super().get_queryset().filter(owner=self.request.user)

class TaskListView(TaskMixinView, ListView):
    model = Task
    ordering = '-date_of_creation'

class TaskUpdateView(TaskMixinView, UpdateView):
    form_class = TaskForm
    model = Task

class TaskCreateView(TaskMixinView, CreateView):
    form_class = TaskForm
    model = Task
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        return super().form_valid(form)
    
class TaskDeleteView(TaskMixinView, DeleteView):
    model = Task
    success_url = reverse_lazy('todo:list')
