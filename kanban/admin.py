from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'due_date')

admin.site.register(Task, TaskAdmin)