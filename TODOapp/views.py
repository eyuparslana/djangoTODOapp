from django.shortcuts import render, redirect
from django.contrib.auth.views import login_required
from .models import Todo
from django.contrib.auth.models import User
import csv
import os
from django.http import HttpResponse


@login_required
def todo_view(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'active_user': request.user
    }
    return render(request, 'todoapp/home.html', context)


@login_required
def profile_view(request):
    if request.POST:
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']

        if not username:
            return render(request, 'todoapp/profile.html', {'error': 'Username cannot blank'})
        user = User.objects.get(username=username)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return render(request, 'todoapp/profile.html', {'info': 'User informations updated.'})
    return render(request, 'todoapp/profile.html', {'user': request.user})


def add_todo(request):
    if request.POST:
        todo = request.POST['todo']
        status = request.POST['status']
        user = request.user
        if not todo:
            todos = Todo.objects.all()
            context = {
                'todos': todos,
                'error': 'todo is required'
            }
            return render(request, 'todoapp/home.html', context)
        new_todo = Todo(user=user, text=todo, is_completed=status)
        new_todo.save()
        return redirect('/todo/')
    return redirect('/todo/')


def status(request):
    pass


def export_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="todo.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'Todo', 'Status', 'Created', 'Updated'])

    todos = Todo.objects.all()
    for todo in todos:
        writer.writerow([todo.user, todo.text, todo.is_completed, todo.created, todo.modified])
    return response


def import_view(request):
    if request.POST:
        path = request.FILES['path']

        if not path.name.endswith('.csv'):
            return HttpResponse("Please enter .csv file")
        file = request.FILES['path']
        file_data = file.read().decode('utf-8')
        lines = file_data.split('\n')[1:]

        for line in lines:
            if not line:
                break
            todo = line.split(',')[0]
            if line.split(',')[1] == 'Completed':
                todo_status = True
            else:
                todo_status = False
            new_todo = Todo(user=request.user, text=todo, is_completed=todo_status)
            new_todo.save()
    return redirect('/todo/')
