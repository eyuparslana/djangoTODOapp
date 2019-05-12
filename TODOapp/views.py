from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.views import login_required
from .models import Todo
from django.contrib.auth.models import User
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator


@login_required
def todo_view(request):
    todos = Todo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(todos, 5)
    context = {
        'todos': paginator.page(page),
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


@login_required
def add_todo(request):
    if request.POST:
        todo = request.POST['todo']
        status = request.POST['status']
        user = request.user
        if not todo:
            todos = Todo.objects.all()
            context = {
                'active_user': user,
                'todos': todos,
                'error': 'todo is required'
            }
            return render_to_response('todoapp/home.html', context)
        new_todo = Todo(user=user, text=todo, is_completed=status)
        new_todo.save()
        return redirect('/todo/')
    return redirect('/todo/')


def status(request):
    if request.POST:
        for k, v in request.POST.items():
            if k.startswith('stodo'):
                todo_id = int(k[5:])
                todo = Todo.objects.get(id=todo_id)
                if todo.is_completed:
                    todo.is_completed = False
                else:
                    todo.is_completed = True
                todo.save()
                return redirect('/todo/')
            elif k.startswith('dtodo'):
                todo_id = int(k[5:])
                todo = Todo.objects.get(id=todo_id)
                todo.delete()
                return redirect('/todo/')
    return redirect('/todo/')

@login_required
def export_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="todo.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'Todo', 'Status', 'Created', 'Updated'])

    todos = Todo.objects.all()
    for todo in todos:
        writer.writerow([todo.user, todo.text, todo.is_completed, todo.created, todo.modified])
    return response

@login_required
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


@login_required
def statistics_view(request):
    completed_todo_count = Todo.objects.filter(user=request.user, is_completed=True).count()
    not_completed_todo_count = Todo.objects.filter(user=request.user, is_completed=False).count()
    context = {
        'completed': completed_todo_count,
        'not_completed': not_completed_todo_count
    }
    return render(request, 'todoapp/statistic.html', context)
