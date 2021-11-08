from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .serializers import RegisterSerializer
from apps.users.serializers import UserDetailSerializer

UserModel = get_user_model()


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class EmailActivateView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        token = self.request.query_params.get('token')
        try:
            token = RefreshToken(token)
            user_id = token.payload.get('user_id')
            token.blacklist()
        except TokenError as err:
            return Response({'error': str(err)}, status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(UserModel, pk=user_id)
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
