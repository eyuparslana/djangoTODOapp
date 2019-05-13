from django.urls import path, include
from . import views


urlpatterns = [
    path('todo/', views.todo_view, name='todos'),
    path('profile/', views.profile_view, name='profile'),
    path('todo/add/', views.add_todo, name='add'),
    path('todo/status/', views.status, name='status'),
    path('todo/export', views.export_view, name='export'),
    path('todo/import', views.import_view, name='import'),
    path('todo/statistics', views.statistics_view, name='statistics')
]