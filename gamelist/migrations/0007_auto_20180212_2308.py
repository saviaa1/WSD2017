# Generated by Django 2.0.1 on 2018-02-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0006_auto_20180206_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_url',
            field=models.URLField(default="{% static '/question.png' %}"),
        ),
    ]