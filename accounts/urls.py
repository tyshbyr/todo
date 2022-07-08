from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('create-done/', views.UserCreateDoneView.as_view(), name='user_create_done'),
    path('activate/<uidb64>/<token>/', views.UserActivateView.as_view(), name='user_activate'),
    path('detail/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('delete/<int:pk>', views.UserDeleteView.as_view(), name='user_delete'),
]
