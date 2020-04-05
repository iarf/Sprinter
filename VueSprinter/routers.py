from rest_framework import routers
from sprinter.views import ProjectView, TaskView

router = routers.DefaultRouter()

router.register('projects', ProjectView)
router.register('tasks', TaskView)
