from rest_framework import serializers

from ..auth_.serializers import MyUserSerializer
from .models import Task, TaskList


class TaskListSerializer(serializers.ModelSerializer):
    owner = MyUserSerializer(read_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'owner',)


class TaskSerializer(serializers.ModelSerializer):

    list = TaskListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
