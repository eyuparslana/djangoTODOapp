from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'is_completed', 'created', 'modified')
    search_fields = ('user', 'text')
    list_filter = ('user', 'is_completed', 'created', 'modified')
    list_display_links = ('text',)
