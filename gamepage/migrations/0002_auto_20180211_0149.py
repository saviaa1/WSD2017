# Generated by Django 2.0.2 on 2018-02-10 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='gameState',
            field=models.TextField(null=True),
        ),
    ]
