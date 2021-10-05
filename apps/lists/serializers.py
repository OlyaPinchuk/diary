from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import ListModel, ListItemModel


# class ListSerializer(ModelSerializer):
#     class Meta:
#         model = ListModel
#         fields = ('id', 'title')
#
#
# class ListItemSerializer(ModelSerializer):
#     class Meta:
#         model = ListItemModel
#         fields = ('id', 'content', 'list')


class ItemSerializer(ModelSerializer):
    class Meta:
        model = ListItemModel
        fields = ('id', 'content')


class ListSerializer(ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = ListModel
        fields = ('id', 'title', 'user', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        list = ListModel.objects.create(**validated_data)
        for item_data in items_data:
            ListItemModel.objects.create(list=list, **item_data)
        return list