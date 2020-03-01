from django.urls import path
from .views import TaskList, TaskRetrieveUpdateDelete

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDelete.as_view()),

]