from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from .views import RegisterMyUserAPIView, MyUserViewSet, SellerListView, CustomerListView

# router = DefaultRouter()
# router.register('user', MyUserViewSet, basename='user')


urlpatterns = {
    path('login/', obtain_jwt_token),
    # path('register/', RegisterMyUserAPIView.as_view()),
    path('seller/', SellerListView.as_view()),
    path('customer/', CustomerListView.as_view()),
}

# urlpatterns += router.urls
