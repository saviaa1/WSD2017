# Generated by Django 2.0.1 on 2018-01-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='role',
            new_name='developer',
        ),
    ]
