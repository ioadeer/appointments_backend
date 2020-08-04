from django.urls import path, include 
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('appointments.urls')),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
