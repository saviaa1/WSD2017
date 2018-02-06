# Generated by Django 2.0.1 on 2018-02-06 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20180201_0927'),
        ('gamelist', '0002_game_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='user',
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Profile'),
        ),
    ]
