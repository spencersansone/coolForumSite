# Generated by Django 2.0.3 on 2018-07-13 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_forumpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='ForumPost',
        ),
    ]
