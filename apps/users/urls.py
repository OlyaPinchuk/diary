from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListView, UserUpToAdminView, UserUpdateProfileView, ChosenUserListView
from ..notes.views import UserNotes

urlpatterns = [
    path('', UserListView.as_view(), name='all_users'),
    path('/<int:pk>/to_admin', UserUpToAdminView.as_view(), name='up_to_admin'),
    path('/<int:pk>/profile', UserUpdateProfileView.as_view(), name='update_profile'),
    path('/<int:pk>', ChosenUserListView.as_view()),
    path('/<int:pk>/notes', UserNotes.as_view())
]
