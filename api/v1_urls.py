from django.urls import path, include

urlpatterns = [
    path('/auth_', include('apps.auth_.urls')),
    path('/users', include('apps.users.urls')),
    path('/profile', include('apps.user_profile.urls'))
]