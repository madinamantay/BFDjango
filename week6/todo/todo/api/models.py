from django.db import models

# from ..auth_.models import MyUser
# import sys
# sys.path.append("..")
# Create your models here.
from ..auth_.models import MyUser
from django.utils import timezone


class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class TaskList(models.Model):
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    objects = TaskManager()

    class Meta:
        verbose_name = 'Task list'
        verbose_name_plural = 'Tasks list'

    def __str__(self):
        return f'{self.name} task list'


class Task(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    due_on = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    notes = models.CharField(max_length=255, default='', blank=True)

    objects = TaskManager()

    class Meta:
        verbose_name = 'Task item'
        verbose_name_plural = 'Task items'

    def __str__(self):
        return f'{self.title}, in {self.list}'
