from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)

    class Meta:
        model = Task
        fields = '__all__'
