# Generated by Django 4.2.7 on 2024-01-07 18:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_delete_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ManyToManyField(blank=True, related_name='my_follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(related_name='is_following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
