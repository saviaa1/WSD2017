# Generated by Django 2.0.1 on 2018-02-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0007_auto_20180212_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_url',
            field=models.URLField(default='/question.png'),
        ),
    ]
