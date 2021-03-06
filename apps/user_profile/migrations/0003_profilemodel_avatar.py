# Generated by Django 3.2.5 on 2021-11-15 15:54

import apps.user_profile.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_profilemodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(default='../../images/avatar.jpg', upload_to=apps.user_profile.services.avatar_upload),
        ),
    ]
