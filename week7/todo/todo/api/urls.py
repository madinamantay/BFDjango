from django.urls import path
# from .views import TaskListView, TaskListView2, TaskView, TaskView2
from rest_framework.routers import DefaultRouter
from .views import TaskListViewSet, TaskViewSet

router = DefaultRouter()

router.register(r'', TaskListViewSet, basename='list')
router.register(r'task', TaskViewSet, basename='list-task')

urlpatterns = router.urls
#
# urlpatterns = [
#     path('', TaskListView.as_view()),
#     path('<int:pk>/', TaskListView2.as_view()),
#     path('<int:pk>/task/', TaskView.as_view()),
#     path('<int:pk>/task/<int:pk2>/', TaskView2.as_view()),
#
# ]
