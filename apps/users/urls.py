from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListView, UserUpToAdminView, UserUpdateProfileView, ChosenUserView
from ..lists.views import UserListsView, ChosenListView, UserChosenList
from ..notes.views import UserNotes, ChosenNote

urlpatterns = [
    path('', UserListView.as_view(), name='all_users'),
    path('/<int:pk>/to_admin', UserUpToAdminView.as_view(), name='up_to_admin'),
    path('/<int:pk>/profile', UserUpdateProfileView.as_view(), name='update_profile'),
    path('/<int:pk>', ChosenUserView.as_view()),
    path('/<int:pk>/notes', UserNotes.as_view()),
    path('/<int:pk>/lists', UserListsView.as_view()),
]
