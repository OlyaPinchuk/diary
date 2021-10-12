from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NoteSerializer
from .models import NoteModel


class NoteCreate(CreateAPIView):
    serializer_class = NoteSerializer


class NoteListView(ListAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


class UserNotes(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        db_notes = NoteModel.objects.filter(user_id=pk)
        # db_notes = get_object_or_404(NoteModel.objects.all(), user_id=pk) # does not work
        notes = NoteSerializer(db_notes, many=True).data
        return Response(notes, status.HTTP_200_OK)


class ChosenNote(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        id = kwargs.get('id')
        note = get_object_or_404(NoteModel.objects.all(), pk=id)
        data = NoteSerializer(note).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        id = kwargs.get('id')
        note = get_object_or_404(NoteModel.objects.all(), pk=id)
        serializer = NoteSerializer(note, self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
