from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ListModel(models.Model):
    class Meta:
        db_table = 'list'

    title = models.CharField(max_length=100)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)


class ListItemModel(models.Model):
    class Meta:
        db_table = 'list_item'

    list = models.ForeignKey(ListModel, related_name='items', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    status = models.BooleanField(default=False)


