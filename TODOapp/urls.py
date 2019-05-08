from django.urls import path, include
from django.contrib.auth import login
from . import views


urlpatterns = [
    path('', views.todo_view, name='todos'),
]