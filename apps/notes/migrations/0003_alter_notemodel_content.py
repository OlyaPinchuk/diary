# Generated by Django 3.2.5 on 2021-11-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='content',
            field=models.CharField(max_length=5000),
        ),
    ]
