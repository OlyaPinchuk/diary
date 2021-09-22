from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import ListModel


class ListSerializer(ModelSerializer):
    class Meta:
        model = ListModel
        fields = ('id', 'title')