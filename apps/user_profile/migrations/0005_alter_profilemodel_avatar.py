# Generated by Django 3.2.5 on 2021-11-15 17:40

import apps.user_profile.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_profilemodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(default='../../images/avatar.jpg', upload_to=apps.user_profile.services.avatar_upload),
        ),
    ]