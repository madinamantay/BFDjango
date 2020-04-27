from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MyUserSerializer
from .models import MyUser


class RegisterMyUserAPIView(APIView):
    http_method_names = ['post']
    permission_classes = (IsAdminUser, )

    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyUserSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class SellerListView(mixins.ListModelMixin,
                       generics.GenericAPIView):
    http_method_names = ['get']
    queryset = MyUser.objects.get_salesmen()
    serializer_class = MyUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomerListView(mixins.ListModelMixin,
                        generics.GenericAPIView):
    http_method_names = ['get']
    queryset = MyUser.objects.get_customers()
    serializer_class = MyUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)