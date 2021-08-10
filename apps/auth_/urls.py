from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth_.views import RegisterView, EmailActivateView


urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='tokens'),
    path('/activate', EmailActivateView.as_view(), name='activate_by_email'),
    path('/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('/register', RegisterView.as_view(), name='register_user')
]