from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import viewsets, generics
from django.shortcuts import render
# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
