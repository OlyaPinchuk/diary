from django.urls import path


from .views import NoteListView, NoteCreate

urlpatterns = [
    path('', NoteListView.as_view()),
    path('/add', NoteCreate.as_view()),
]