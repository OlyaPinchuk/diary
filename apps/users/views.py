from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsSuperUser
from .serializers import UserDetailSerializer, ProfileDetailSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

UserModel = get_user_model()


class UserListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserModel.objects.all()
    serializer_class = UserDetailSerializer


class ChosenUserView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel.objects.all(), pk=pk)
        data = UserDetailSerializer(user).data
        return Response(data, status.HTTP_200_OK)


class UserUpToAdminView(GenericAPIView):
    queryset = UserModel.objects
    permission_classes = [IsSuperUser]

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUpdateProfileView(UpdateAPIView):
    serializer_class = ProfileDetailSerializer

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_object(self):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        print(user.profile.avatar)
        return user.profile
