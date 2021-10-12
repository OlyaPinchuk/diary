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


class UserListsView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        db_lists = ListModel.objects.filter(user_id=pk)
        lists = ListSerializer(db_lists, many=True).data
        return Response(lists, status.HTTP_200_OK)


class ChosenListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        id = kwargs.get('id')
        list = get_object_or_404(ListModel.objects.all(), pk=id)
        data = ListSerializer(list).data
        return Response(data, status.HTTP_200_OK)


class UserChosenList(APIView):

    def get(self, *args, **kwargs):
        user_id = kwargs.get('pk')
        list_id = kwargs.get('id')
        db_lists = ListModel.objects.filter(user_id=user_id)
        chosen_list = 0
        for l in db_lists:
            print(l)
            if l.id == list_id:
                chosen_list = l
        data = ListSerializer(chosen_list).data
        return Response(data, status.HTTP_200_OK)




