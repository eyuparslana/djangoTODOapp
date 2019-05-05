from django.urls import path, include
from TODOapp import views
from django.contrib.auth import views

urlpatterns = [
    path("todo/login/", views.LoginView.as_view(), name='login')
]