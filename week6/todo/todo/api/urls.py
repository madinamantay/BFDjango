from django.urls import path
from .views import TaskListView, TaskListView2, TaskView, TaskView2

urlpatterns = [
    path('', TaskListView.as_view()),
    path('<int:pk>/', TaskListView2.as_view()),
    path('<int:pk>/task/', TaskView.as_view()),
    path('<int:pk>/task/<int:pk2>/', TaskView2.as_view()),

]
