from django.urls import path

# from .views import ListCreate, ListListView,
from .views import GetListView, CreateListView

urlpatterns = [
    # path('', ListListView.as_view()),
    # path('/add', ListCreate.as_view()),
    path('', GetListView.as_view()),
    path('/add', CreateListView.as_view())

]