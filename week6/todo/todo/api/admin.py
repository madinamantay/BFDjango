from django.contrib import admin
from .models import Task, TaskList


# Register your models here.
@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'created_at', 'notes', 'is_done', )