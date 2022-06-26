from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

class TaskUpdateView(UpdateView):
    form_class = TaskForm
    model = Task

class TaskCreateView(CreateView):
    form_class = TaskForm
    model = Task
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo:list')
    