# Generated by Django 2.0.1 on 2018-02-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20180201_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]