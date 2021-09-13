from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import NoteModel


class NoteCreate(CreateAPIView):
    serializer_class = NoteSerializer


class NoteListView(ListAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
