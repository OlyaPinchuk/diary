from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import NoteModel

UserModel = get_user_model()


class NoteSerializer(ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ('id', 'title', 'content')


