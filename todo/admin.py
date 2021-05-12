from todo.models import Todo
from django.contrib import admin

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")

admin.site.register(Todo, TodoAdmin)
