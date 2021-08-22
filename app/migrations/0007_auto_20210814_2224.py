# Generated by Django 3.1.3 on 2021-08-15 03:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20210814_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='logo',
        ),
        migrations.AddField(
            model_name='post',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]