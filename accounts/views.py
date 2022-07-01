from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import User
from .forms import UserCreationForm


class UserCreateView(CreateView):
    form_class = UserCreationForm
    model = User
    success_url = reverse_lazy('todo:login')
