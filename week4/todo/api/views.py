from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


# Create your views here.


class TaskList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskSerializer


class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskSerializer
