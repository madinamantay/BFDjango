from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet, ProductCreateView
from .views import ProductOrderApiView, ProductOrderDetailApiView, OfferListApiView


urlpatterns = [
    path('product/', ProductCreateView.as_view()),
    path('orders/', ProductOrderApiView.as_view()),
    path('orders/<int:pk>/', ProductOrderDetailApiView.as_view()),
    path('offers/', OfferListApiView.as_view()),
]

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
urlpatterns += router.urls