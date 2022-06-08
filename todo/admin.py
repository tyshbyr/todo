from django.utils import timezone
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = (('title', 'date_of_creation'), 'description', ('deadline', 'date_of_completion'), ('status', 'owner'))
    readonly_fields = ('date_of_creation', 'date_of_completion', 'owner')
    list_display = ('title', 'date_of_creation', 'deadline', 'date_of_completion', 'status')
    list_editable = ('deadline', 'status')
    search_fields = ('title',)
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        if obj.status == 'Completed':
            obj.date_of_completion = timezone.now()
        else:
            obj.date_of_completion = None
        super().save_model(request, obj, form, change)

admin.site.register(Task, TaskAdmin)
