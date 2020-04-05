from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name','description','points','status','project']


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Project
        fields = ['id','name','description','owner', 'users', 'tasks']
