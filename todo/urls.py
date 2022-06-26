from django.urls import path

from . import views


app_name = 'todo'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
]
