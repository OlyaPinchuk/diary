from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class NoteModel(models.Model):
    class Meta:
        db_table = 'note'

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    # user = models.ManyToOneRel(UserModel, related_name='note')


