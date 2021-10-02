from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ListSerializer
from .models import ListModel


# class ListCreate(CreateAPIView):
#     serializer_class = ListSerializer
#
#
# class ListListView(ListAPIView):
#     queryset = ListModel.objects.all()
#     serializer_class = ListSerializer
#     # permission_classes = [IsAuthenticated]


class GetListView(APIView):

    def get(self, *args, **kwargs):
        db_lists = ListModel.objects.all()
        lists = ListSerializer(db_lists, many=True).data
        return Response(lists, status.HTTP_200_OK)


class CreateListView(APIView):

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ListSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)