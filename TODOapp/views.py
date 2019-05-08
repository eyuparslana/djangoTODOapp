from django.shortcuts import render, redirect
from django.contrib.auth.views import login_required
from .models import Todo


@login_required
def todo_view(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'active_user': request.user
    }
    return render(request, 'todoapp/home.html', context)
