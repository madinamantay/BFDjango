from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Task, TaskList
from .serializers import TaskSerializer, TaskListSerializer


# Create your views here.
class TaskListViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(list=self.kwargs.get('parent_lookup_list'))

    def get_serializer_class(self):
        return TaskSerializer

    def perform_create(self, serializer):
        list_id = self.kwargs.get('parent_lookup_list')
        serializer.save(list=TaskList.objects.get(id=list_id))

class TaskListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class TaskListView2(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user).filter(id=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return TaskListSerializer


class TaskView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(list=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return TaskSerializer

    def perform_create(self, serializer):
        list_id = self.kwargs.get('pk')
        serializer.save(list=TaskList.objects.get(id=list_id))


class TaskView2(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs.get('pk'), list=self.kwargs.get('pk2'))

    def get_serializer_class(self):
        return TaskSerializer
