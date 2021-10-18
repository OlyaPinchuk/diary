from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import ListModel, ListItemModel


class ItemSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = ListItemModel
        fields = ('id', 'content', 'status')


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


    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        for item_data in items_data:
            obj, created = ListItemModel.objects.update_or_create(
                id=item_data.get('id'),
                defaults={"content": item_data.get('content'), "list_id": instance.id}
            )
        instance.title = validated_data.get('title', instance.title)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        return instance
