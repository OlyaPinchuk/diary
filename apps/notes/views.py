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

    # def get(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     db_notes = NoteModel.objects.filter(user_id=pk)
    #     # db_notes = get_object_or_404(NoteModel.objects.all(), user_id=pk) # does not work
    #     notes = NoteSerializer(db_notes, many=True).data
    #     return Response(dict(notes='notes'), status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        page = int(request.GET.get('pageIndex'))
        step = 5
        db_notes = NoteModel.objects.filter(user_id=pk)[step*page:step*page+step]
        # db_notes = NoteModel.objects.filter(user_id=pk)[1:5]
        notes = NoteSerializer(db_notes, many=True).data
        number = NoteModel.objects.filter(user_id=pk).count()
        response = {
            "number": number,
            "notes": notes
        }
        return Response(response, status.HTTP_200_OK)


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

    def delete(self, *args, **kwargs):
        id = kwargs.get('id')
        note = get_object_or_404(NoteModel.objects.all(), pk=id)
        note.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class FoundNotesListView(APIView):

    def get(self, request, *args, **kwargs):
        found_notes = []
        page = int(request.GET.get('pageIndex'))
        step = 5
        search_text = request.GET.get('searchText').lower()
        user_id = request.GET.get('userId')
        db_notes = NoteModel.objects.filter(user_id=user_id)
        notes = NoteSerializer(db_notes, many=True).data
        for n in notes:
            if search_text in n['title'].lower():
                found_notes.append(n)
                print('found', n['title'])
        number = len(found_notes)
        found_notes = found_notes[step*page:step*(page+1)]
        response = {
            "number": number,
            "notes": found_notes
        }
        return Response(response, status.HTTP_200_OK)


class UserNotesPaginatedListView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        db_notes = NoteModel.objects.filter(user_id=pk)
        # db_notes = get_object_or_404(NoteModel.objects.all(), user_id=pk) # does not work
        notes = NoteSerializer(db_notes, many=True).data
        return Response(notes, status.HTTP_200_OK)
