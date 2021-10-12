from django.urls import path


from .views import NoteListView, NoteCreate, ChosenNote

urlpatterns = [
    path('', NoteListView.as_view()),
    path('/add', NoteCreate.as_view()),
    path('/<int:id>', ChosenNote.as_view())
]