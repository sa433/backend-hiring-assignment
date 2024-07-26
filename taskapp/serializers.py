from rest_framework import serializers
from taskapp.models import ClientModel, ProjectModel, TaskModel

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'