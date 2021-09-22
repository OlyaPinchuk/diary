from django.urls import path

from .views import ListCreate, ListListView

urlpatterns = [
    path('', ListListView.as_view()),
    path('/add', ListCreate.as_view())
]