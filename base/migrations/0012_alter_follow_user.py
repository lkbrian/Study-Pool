# Generated by Django 4.2.7 on 2024-01-09 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_follow_user_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]