from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ListSerializer, ItemSerializer
from .models import ListModel, ListItemModel


class GetListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, *args, **kwargs):
        db_lists = ListModel.objects.all()
        lists = ListSerializer(db_lists, many=True).data
        return Response(lists, status.HTTP_200_OK)


class CreateListView(APIView):

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserListsView(APIView):

    # def get(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     db_lists = ListModel.objects.filter(user_id=pk)
    #     lists = ListSerializer(db_lists, many=True).data
    #     return Response(lists, status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        page = int(request.GET.get('pageIndex'))
        step = 5
        db_lists = ListModel.objects.filter(user_id=pk)[step*page:step*page+step]
        lists = ListSerializer(db_lists, many=True).data
        number = ListModel.objects.filter(user_id=pk).count()
        response = {
            "number": number,
            "lists": lists
        }
        return Response(response, status.HTTP_200_OK)


class ChosenListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        id = kwargs.get('id')
        list = get_object_or_404(ListModel.objects.all(), pk=id)
        data = ListSerializer(list).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        id = kwargs.get('id')
        list = get_object_or_404(ListModel.objects.all(), pk=id)
        serializer = ListSerializer(list, self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        list_id = kwargs.get('id')
        list = get_object_or_404(ListModel.objects.all(), pk=list_id)
        list.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class UserChosenList(APIView):

    def get(self, *args, **kwargs):
        user_id = kwargs.get('pk')
        list_id = kwargs.get('id')
        db_lists = ListModel.objects.filter(user_id=user_id)
        chosen_list = 0
        for l in db_lists:
            if l.id == list_id:
                chosen_list = l
        data = ListSerializer(chosen_list).data
        return Response(data, status.HTTP_200_OK)


class ListItemView(APIView):

    def put(self, *args, **kwargs):
        item_id = kwargs.get('itemId')
        item = get_object_or_404(ListItemModel.objects.all(), pk=item_id)
        serializer = ItemSerializer(item, self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        item_id = kwargs.get('itemId')
        db_item = ListItemModel.objects.filter(pk=item_id)
        db_item.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class FoundListsListView(APIView):

    def get(self, request, *args, **kwargs):
        found_lists = []
        page = int(request.GET.get('pageIndex'))
        step = 5
        search_text = request.GET.get('searchText').lower()
        user_id = request.GET.get('userId')
        if request.GET.get('sortOption'):
            sort_option = int(request.GET.get('sortOption'))
            print(sort_option)
            db_lists = ListModel.objects.filter(user_id=user_id)
            lists = ListSerializer(db_lists, many=True).data
            for l in lists:
                if search_text in l['title'].lower():
                    found_lists.append(l)
            number = len(found_lists)
            if sort_option == 1:
                print('if 1')
                def sort_func(e):
                    return len(e['items'])
                found_lists.sort(reverse=True, key=sort_func)
            elif sort_option == 0:
                print('if 1')
                def sort_func(e):
                    return len(e['items'])
                found_lists.sort(reverse=False, key=sort_func)

            # found_lists = found_lists[step * page:step * (page + 1)]
            response = {
                "number": number,
                "lists": found_lists[step * page:step * (page + 1)]
            }
            return Response(response, status.HTTP_200_OK)
        else:
            db_lists = ListModel.objects.filter(user_id=user_id)
            lists = ListSerializer(db_lists, many=True).data
            for l in lists:
                if search_text in l['title'].lower():
                    found_lists.append(l)
                    print('found', l['title'])
            number = len(found_lists)
            found_lists = found_lists[step*page:step*(page+1)]
            response = {
                "number": number,
                "lists": found_lists
            }
            return Response(response, status.HTTP_200_OK)


class SortedListsListView(APIView):

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('userId')
        page = int(request.GET.get('pageIndex'))
        step = 5

        def sort_func(e):
            return len(e['items'])

        if request.GET.get('sortOption'):
            sort_option = int(request.GET.get('sortOption'))
            if sort_option == 1:
                db_lists = ListModel.objects.filter(user_id=pk)
                lists = ListSerializer(db_lists, many=True).data
                lists.sort(reverse=True, key=sort_func)
            elif sort_option == 0:
                db_lists = ListModel.objects.filter(user_id=pk)
                lists = ListSerializer(db_lists, many=True).data
                lists.sort(reverse=False, key=sort_func)

        return Response(lists[step*page:step*(page+1)], status.HTTP_200_OK)


