from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    points = models.DecimalField(max_digits=3, decimal_places=1)
    status = models.IntegerField()
