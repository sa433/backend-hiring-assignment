from django.contrib import admin
from taskapp.models import ClientModel, TaskModel, ProjectModel

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'tname', 'tdesc', 'proj_name', 'status']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'pdesc', 'client', 'start_date', 'end_date']

admin.site.register(ClientModel, ClientAdmin)
admin.site.register(TaskModel, TaskAdmin)
admin.site.register(ProjectModel, ProjectAdmin)
