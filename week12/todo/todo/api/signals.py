from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TaskList, Task


@receiver(post_save, sender=TaskList)
def create_task_in_task_list(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(name='Empty task', list=instance)
