from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from .serializers import MyUserSerializer
from .models import MyUser


class UserCreateViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return MyUserSerializer
