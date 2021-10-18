from django.urls import path

from .views import GetListView, CreateListView, ChosenListView

urlpatterns = [
    path('', GetListView.as_view()),
    path('/add', CreateListView.as_view()),
    path('/<int:id>', ChosenListView.as_view()),
    path('/<int:id>/edit', ChosenListView.as_view()),
    path('/<int:id>/delete', ChosenListView.as_view()),

]