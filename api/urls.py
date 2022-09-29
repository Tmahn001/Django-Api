from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views
from .views import MyTokenObtainPairView, MyTokenObtainPairSerializer

urlpatterns = [
    path('', views.getData),
    path('view', views.addItem, name='sample'),
    path('test', views.getRoutes,),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]