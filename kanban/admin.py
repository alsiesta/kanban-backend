from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'due_date')
    def has_delete_permission(self, request, obj=None):
        # Return False to disable delete permission
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not self.has_delete_permission(request):
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions
    
admin.site.register(Task, TaskAdmin)