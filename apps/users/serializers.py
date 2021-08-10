from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from apps.user_profile.serializers import ProfileDetailSerializer

UserModel = get_user_model()


class UserDetailSerializer(ModelSerializer):
    profile = ProfileDetailSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'is_staff', 'profile')