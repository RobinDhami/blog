# Generated by Django 5.0.7 on 2024-07-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blogger_likes_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
