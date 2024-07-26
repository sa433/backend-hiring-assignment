from django.db import models

class ClientModel(models.Model):
    cname = models.CharField(max_length=255)

class ProjectModel(models.Model):
    pname = models.CharField(max_length=255)
    pdesc = models.TextField()
    client = models.ForeignKey(ClientModel, related_name='clt', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

status_choice = [
    ('To Do', 'To Do'), 
    ('WIP', 'WIP'),
    ('On Hold', 'On Hold'),
    ('Done', 'DOne')
]

class TaskModel(models.Model):
    tname = models.CharField(max_length=255)
    tdesc = models.CharField(max_length=255, null=True)
    proj_name = models.ForeignKey(ProjectModel, related_name='task', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_choice, default='To Do')


