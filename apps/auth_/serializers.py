from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from ..user_profile.serializers import ProfileCreateSerializer

from enums.regex_enum import RegEx as R
from .utils import Utils

UserModel = get_user_model()


class RegisterSerializer(ModelSerializer):
    profile = ProfileCreateSerializer()
    password = CharField(validators=[RegexValidator(R.PASSWORD.reg, R.PASSWORD.msg)], write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'profile')

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        token = Utils.create_email_token(user)
        data = {
            'subject': 'Activate account',
            'body': f'http://django-env.eba-tfm4buue.us-west-2.elasticbeanstalk.com/api/v1/auth_/activate?token={token}',
            'to': [user.email]
        }
        Utils.send_email(**data)
        serializer = ProfileCreateSerializer(data=profile)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return user