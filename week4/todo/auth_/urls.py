from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .views import RegisterUserApiView, UserViewSet


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', RegisterUserApiView.as_view())
]
