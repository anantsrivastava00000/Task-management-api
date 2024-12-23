from django.contrib import admin
from .models import *
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'title', 'description', 'completed', 'due_date', 'created_at', 'updated_at']

admin.site.register(Task, TaskAdmin)