# Generated by Django 4.0.6 on 2022-07-09 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
