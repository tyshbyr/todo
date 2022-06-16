from django.utils import timezone
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = (('title', 'date_of_creation'), 'description', ('deadline', 'view_date_of_completion'), ('status',))
    readonly_fields = ('date_of_creation', 'view_date_of_completion')
    list_display = ('title', 'date_of_creation', 'deadline', 'view_date_of_completion', 'status')
    list_editable = ('deadline', 'status')
    search_fields = ('title',)
    
    def view_date_of_completion(self, obj):
        if obj.date_of_completion:
            return obj.date_of_completion
        else:
            return 'Ожидает выполнения'
        
    view_date_of_completion.short_description = 'Дата выполнения'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        if obj.status == 'Completed':
            obj.date_of_completion = timezone.now()
        else:
            obj.date_of_completion = None
        super().save_model(request, obj, form, change)

admin.site.register(Task, TaskAdmin)
