from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ListModel(models.Model):
    class Meta:
        db_table = 'list'

    title = models.CharField(max_length=100)

