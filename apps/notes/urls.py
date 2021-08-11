from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views import NoteListView, NoteCreate

urlpatterns = [
    path('', NoteListView.as_view()),
    path('/add', NoteCreate.as_view())
]