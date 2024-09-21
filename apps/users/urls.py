from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from apps.users.views import UserRegisterAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', UserRegisterAPI, basename='user_register')

urlpatterns = [
    # path('', UserAPIView.as_view(), name='api_users_list'),
    # path('register/', UserRegisterAPIView.as_view(), name='api_users_register'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls