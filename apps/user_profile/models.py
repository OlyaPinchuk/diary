from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators as v

from apps.user_profile.services import avatar_upload
from enums.regex_enum import RegEx as R

UserModel = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=255, validators=[v.RegexValidator(R.NAME.reg, R.NAME.msg)])
    surname = models.CharField(max_length=255, validators=[v.RegexValidator(R.NAME.reg, R.NAME.msg)])
    age = models.IntegerField(validators=[v.MinValueValidator(1), v.MaxValueValidator(150)])
    avatar = models.ImageField(upload_to=avatar_upload, default='../../images/avatar.jpg')
    # avatar = models.FileField(upload_to=avatar_upload, default='../../images/avatar.jpg')
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
