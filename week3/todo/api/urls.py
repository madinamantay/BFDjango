from django.urls import path
from api import views

urlpatterns = [
    path('home', views.index)
]