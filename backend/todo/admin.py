from django.contrib import admin
from todo.models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed',)

admin.site.register(ToDo, ToDoAdmin)
