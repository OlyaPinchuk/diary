from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class NoteModel(models.Model):
    class Meta:
        db_table = 'note'

    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

